#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# Mapping moon phases and illumination percentages to Nerd Font moon phase icons
def get_nerd_font_moon_icon(illumination, phase):
    if phase == 'New Moon' or illumination == 0:
        return "󰽤"
    elif phase == 'Full Moon' or illumination == 100:
        return "󰽢"
    elif "Waxing" in phase:
        if illumination < 10:
            return ""
        elif illumination <20:
            return ""
        elif illumination <30:
            return ""
        elif illumination <40:
            return ""
        elif illumination <50:
            return ""
        elif illumination == 50:
            return ""
        elif illumination > 50:
            return ""
        elif illumination >60:
            return "" 
        elif illumination >70:
            return ""
        elif illumination >80:
            return ""
        elif illumination >90:
            return ""
    elif "Waning" in phase:
        if illumination > 50:
            return '\uf09A'  # 🌖 Waning Gibbous
        elif illumination == 50:
            return ""
        elif illumination < 50:
            return '\uf09C'  # 🌘 Waning Crescent
    return 'Unknown Phase'

# Function to scrape the current moon phase and illumination from moongiant.com
def get_moon_phase_and_illumination():
    url = 'https://www.moongiant.com/phase/today/'
    
    try:
        # Adding a timeout to prevent hanging
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error while making the request: {e}")
        return None, None
    
    if response.status_code != 200:
        print(f"Failed to load page, status code: {response.status_code}")
        return None, None
    
    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the <td> element with the id "today_"
    moon_phase_td = soup.find('td', id='today_')
    if not moon_phase_td:
        print("Could not find the moon phase data in the table cell.")
        return None, None
    
    # Extract the alt text from the <img> tag, which contains the moon phase
    moon_img = moon_phase_td.find('img')
    if not moon_img or 'alt' not in moon_img.attrs:
        print("Could not find the moon phase image or its alt text.")
        return None, None
    
    # Extract moon phase from the alt text
    alt_text = moon_img['alt']
    moon_phase = alt_text.split(' on ')[0]  # Get the phase part before the date
    
    # Extract illumination percentage (within a <span> tag in the same <td>)
    illumination_text = moon_phase_td.find('span').text.strip()
    illumination = int(illumination_text.replace('%', '').strip())  # Convert to integer
    
    return moon_phase, illumination

# Main function
if __name__ == '__main__':
    try:
        # Get the current moon phase and illumination percentage
        moon_phase, illumination = get_moon_phase_and_illumination()
        if moon_phase is None or illumination is None:
            print("Could not retrieve the moon phase or illumination.")
        else:
            # Get the corresponding Nerd Font icon based on phase and illumination
            moon_icon = get_nerd_font_moon_icon(illumination, moon_phase)
            # Print the moon phase, illumination, and icon
            print(f"{moon_icon} {moon_phase} {illumination}%")
            print(f"Illumination: {illumination}%")
            print(f"Nerd Font Icon: {moon_icon}")
    except Exception as e:
        print(f"Error: {e}")

