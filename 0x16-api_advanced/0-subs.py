#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API and returns the number of subscribers
  for a given subreddit. It returns 0 for invalid subreddits or errors.

  Args:
      subreddit: The name of the subreddit to query (string).

  Returns:
      The number of subscribers for the subreddit (integer), or 0 if an error occurs.
  """

  # Set a custom User-Agent header to avoid throttling
  headers = {'User-Agent': 'My Reddit API Scraper v1.0 (by your_username)'}

  # Build the URL with specified subreddit
  url = f"https://www.reddit.com/r/{subreddit}/about.json"

  # Make the request without following redirects
  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data for subreddit '{subreddit}': {e}")
    return 0

  # Check for successful response (status code 200)
  if response.status_code == 200:
    data = response.json()
    # Extract the subscriber count from the data (assuming 'data' and 'subscribers' keys exist)
    return data.get('data', {}).get('subscribers', 0)
  else:
    print(f"Error fetching data for subreddit '{subreddit}': Status code {response.status_code}")
    return 0

# Example usage
subreddit_name = "learnpython"  # Replace with the desired subreddit
num_subscribers = number_of_subscribers(subreddit_name)

if num_subscribers > 0:
  print(f"The subreddit '{subreddit_name}' has {num_subscribers} subscribers.")
else:
  print(f"Could not find information for subreddit '{subreddit_name}'.")
