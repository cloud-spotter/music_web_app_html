from playwright.sync_api import Page, expect
from lib.album import *
from lib.album_repository import *

# Tests for your routes go here
'''
When we visit /albums
We see a list of albums by title, with release years
'''
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/album_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Title: Father of the Bride",
        "Title: London Calling",
    ])
    expect(paragraph_tags).to_have_text([
        "Released: 2019", 
        "Released: 1979"
    ])
'''
When we visit /albums/<number>
We see a single album linked to that index number
'''
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/album_store.sql')
    #Try for /albums/1 first (then add string interpolation):
    album_id = 2
    page.goto(f"http://{test_web_address}/albums/{album_id}")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text(f"Title: London Calling")
    expect(paragraph_tags).to_have_text(f"Released: 1979")

#NB artist field not implemented

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
