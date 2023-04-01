from Crawler import crawl_scrape

def main():
    print("This is my main method")
    seed_url = "https://medium.com/"
    crawl_scrape(seed_url)

if __name__ == "__main__":
    main()
