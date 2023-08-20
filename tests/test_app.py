from playwright.sync_api import Page, expect
from lib.album import *
from lib.album_repository import *

# Tests for your routes go here
## ---- Section 02 Exercise ---- ##
'''
When we visit /albums
We see a list of albums by title, with release years
'''
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/album_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Father of the Bride",
        "London Calling", #You do need this comma!
    ])

## ---- Section 02 Challenge ---- ##
'''
When we visit /albums/<number>
We see a single album linked to that index number
'''
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/album_store.sql')
    #Try for /albums/1 first (then add string interpolation):
    album_id = 2
    page.goto(f"http://{test_web_address}/albums/{album_id}")
    h1_tags = page.locator("h1")
    release_year_tag = page.locator(".t-release-year")
    expect(h1_tags).to_have_text(f"London Calling")
    expect(release_year_tag).to_have_text(f"Released: 1979")

#NB artist field not implemented

## ---- Section 03 Exercise ---- ##

'''
The page returned by 'GET /albums' should contain a link for each album listed.
It should link to '/albums/<id>, where <id> is the corresponding album's id.
That page should then show information about the specific album.
'''
def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/album_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    #Add a link
    page.click("text='Father of the Bride'")
    h1_tag = page.locator('h1')
    #Assert what you're expecting to see
    expect(h1_tag).to_have_text('Father of the Bride')
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text('Released: 2019')

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/album_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    #Add a link
    page.click("text='Father of the Bride'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text('Albums')



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
