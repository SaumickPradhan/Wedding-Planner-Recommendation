import os
import pandas as pd
from google.cloud import storage
from app import get_budget, get_event_theme, get_num_people, get_cuisine, get_genre, get_dress_type, get_tier
# from app import submit_form

from flask import session

# To receive input from flask file: 


class GoogleCloudStorage:
    def __init__(self, json_file_path):
        self._client = storage.Client.from_service_account_json(json_file_path)
        self._bucket = self._client.get_bucket('when-we-met-dataset')
        
    def get_blob_as_bytes(self, blob_name):
        return self._bucket.blob(blob_name).download_as_string()
    
    def read_excel_blob_as_dataframe(self, blob_name):
        excel_blob = self.get_blob_as_bytes(blob_name)
        return pd.read_excel(excel_blob)
        
class WeddingPlanner:
    
    #recieve data from flask to run the algorithm on:
    # def recieve_data():
    #     budget = session['budget']
    #     event_theme = session['event_theme']
    #     num_people = session['num_people']
    #     cuisine = session['cuisine']
    #     genre = session['genre']
    #     dress_type = session['dress_type']
    #     tier = session['tier']
    
    def __init__(self, storage_client):
        self._storage_client = storage_client
        
    def get_dataframe_from_blob(self, blob_name):
        return self._storage_client.read_excel_blob_as_dataframe(blob_name)
        
    def match_event_theme_capacity(self, event_df, event_theme, event_capacity):
        return event_df[(event_df['Theme'] == event_theme) & (event_df['Capacity'] == event_capacity)]
    
    def match_cake_tiers(self, cake_df, cake_tiers):
        return cake_df[cake_df['Tiers of Cake'] == cake_tiers]
    
    def match_food_cuisine_diet(self, food_df, food_cuisine, food_diet):
        return food_df[(food_df['Cuisine'] == food_cuisine) & (food_df['dietary specifications'] == food_diet)]
    
    def match_music_type(self, music_df, music_type):
        return music_df[music_df['Type'] == music_type]
    
    def match_wedding_dress_type(self, wedding_dress_df, wedding_dress_type):
        return wedding_dress_df[wedding_dress_df['Type'] == wedding_dress_type]
    
    def get_best_match(self, match_dict):
        max_key = max(match_dict, key=lambda k: len(match_dict[k]))
        best_match_df = pd.DataFrame()
        best_match_df[max_key] = match_dict[max_key]
        del match_dict[max_key]
        for key, value in match_dict.items():
            best_match_df[key] = pd.Series(value)
        return best_match_df
    
    def run(self):
        # Read data from GCP storage
        event_df = self.get_dataframe_from_blob('event.xlsx')
        cake_df = self.get_dataframe_from_blob('cake.xlsx')
        food_df = self.get_dataframe_from_blob('food.xlsx')
        music_df = self.get_dataframe_from_blob('music.xlsx')
        wedding_dress_df = self.get_dataframe_from_blob('wedding_dress.xlsx')
        
        # Get the user input form the flask file
        event_theme = get_event_theme()
        event_capacity = get_num_people()
        food_cuisine = get_cuisine()
        music_type = get_genre()
        wedding_dress_type = get_dress_type()
        cake_tiers = get_tier()
        food_diet = 'vegan'

        
        # # Filter dataframes
        # event_theme = 'Royal'
        # event_capacity = '<50'
        # food_cuisine = 'continental'
        # food_diet = 'vegan'
        # music_type = 'Jazz'
        # wedding_dress_type = 'Romantic'
        # cake_tiers = 3
        
        event_filtered_df = self.match_event_theme_capacity(event_df, event_theme, event_capacity)
        cake_filtered_df = self.match_cake_tiers(cake_df, cake_tiers)
        food_filtered_df = self.match_food_cuisine_diet(food_df, food_cuisine, food_diet)
        music_filtered_df = self.match_music_type(music_df, music_type)
        wedding_dress_filtered_df = self.match_wedding_dress_type(wedding_dress_df, wedding_dress_type)
        
        # Create indexes and zip for each filtered dataframe
        event_index = list(zip(event_filtered_df['Location Name'], event_filtered_df['Cost']))
        cake_index = list(zip(cake_filtered_df['Cake Name'], cake_filtered_df['Cost']))
        venue_index = list(zip(venue_filtered_df['Venue Name'], venue_filtered_df['Cost']))
        # Display available options for each category
        print("Available options for events:")
        for index, option in enumerate(event_index):
            print(f"{index+1}. {option[0]} - ${option[1]}")

        print("\nAvailable options for cakes:")
        for index, option in enumerate(cake_index):
            print(f"{index+1}. {option[0]} - ${option[1]}")

        print("\nAvailable options for venues:")
        for index, option in enumerate(venue_index):
            print(f"{index+1}. {option[0]} - ${option[1]}")
        while True:
            try:
                venue_choice = int(input("\nEnter the number of the venue you'd like to book: "))
                if 1 <= venue_choice <= len(venue_index):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(venue_index))
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and", len(venue_index))

        chosen_venue = venue_index[venue_choice-1][0]
        chosen_cost = venue_index[venue_choice-1][1]

        print("\nYou have chosen to book the", chosen_venue, "venue for your event.")
        print("The cost of the venue is $", chosen_cost)

        # Calculate the total cost of the event
        total_cost = chosen_cost + chosen_cake_cost + chosen_entertainment_cost
        print("\nThe total cost of your event is $", total_cost)

        proceed = input("\nDo you want to proceed with booking this event? (yes/no)")

        if proceed.lower() == 'yes':
            # Save booking details to a file
            with open('booking_details.txt', 'w') as f:
                f.write(f"Event: {chosen_event}\n")
                f.write(f"Venue: {chosen_venue}\n")
                f.write(f"Cake: {chosen_cake}\n")
                f.write(f"Entertainment: {chosen_entertainment}\n")
                f.write(f"Total Cost: ${total_cost}\n")
                print("\nBooking confirmed. Thank you for choosing our service!")
        else:
            print("\nBooking cancelled. Thank you for considering our service.")


