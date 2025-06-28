def fetch_resources(topic):
    """
    Returns a list of mock resource URLs related to the given topic.

    This function generates placeholder links for educational resources
    based on the provided topic. The URLs include links to GeeksforGeeks,
    YouTube search results, and ChatGPT with the topic as a query.

    Note:
        This is a placeholder implementation. In the future, it can be
        replaced with actual Gemini integration or web scraping.

    Parameters:
        topic (str): The topic for which to fetch educational resources.

    Returns:
        list[str]: A list of resource URLs related to the topic.
    """
    
    return [
        f"https://www.geeksforgeeks.org/{topic.replace(' ', '-')}",
        f"https://www.youtube.com/results?search_query={topic}+tutorial",
        f"https://chat.openai.com/?q={topic}"
    ]
