import movie_svc
import requests.exceptions

def main():
    print_header()
    search_event_loop()

def print_header():
    print(f"{'-' * 50}")
    print(f"{'-' * 15} Movie Search App {'-' * 17}")
    print(f"{'-' * 50}\n")

def search_event_loop():
    search = 'Once_through_loop'

    while search != 'x':
        try:
            search = input('Movie search text (enter x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print(f"Found {len(results)} results.")
                for r in results:
                    print(f'{r.year} -- {r.title}')
                print()

        except ValueError as ve:
            print(f"whoops! That didn't happen. Details: You supplied a bad value. -> {ve}")
        except requests.exceptions.ConnectionError as ce:
            print(f"whoops! That didn't happen. Details: Your network might be having issues -> {ce}")
        except Exception as x:
            print(f"You received a spooky error instead of your movie results: {x}")

    print('exiting...')

if __name__ == '__main__':
    main()