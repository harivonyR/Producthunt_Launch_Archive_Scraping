from script.producthunt import scrape_launch_list
from tqdm import tqdm
import io
import contextlib
from utils.dates import build_dates, format_ymd

URL_TEMPLATE = "https://www.producthunt.com/leaderboard/daily/{year}/{month}/{day}"

def scrape_dates(dates_list, show_captured_on_error=True):
    ''' scrape producthunt archive '''
    results = []
    total = len(dates_list)
    
    with tqdm(total=total, desc="Total days", unit="day") as pbar:
        for (y, m, d) in dates_list:
            current_label = format_ymd(y, m, d)
            pbar.set_description_str(f"Scraping {current_label}")
            url = URL_TEMPLATE.format(year=y, month=f"{m:02d}", day=f"{d:02d}")

            # Capture stdout/stderr from scrape_launch_list to avoid breaking tqdm output
            stdout_buf = io.StringIO()
            stderr_buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(stdout_buf), contextlib.redirect_stderr(stderr_buf):
                    products = scrape_launch_list(url)
                # extend results only if function returned iterable/list
                if products:
                    results.extend(products)
            except Exception as exc:
                # Show a concise error without breaking tqdm rendering
                tqdm.write(f"[ERROR] {current_label} -> {exc}")
                if show_captured_on_error:
                    captured_out = stdout_buf.getvalue().strip()
                    captured_err = stderr_buf.getvalue().strip()
                    if captured_out:
                        # show only the last lines to avoid flooding the console
                        tail = "\n".join(captured_out.splitlines()[-10:])
                        tqdm.write(f"[CAPTURED STDOUT — last lines]\n{tail}")
                    if captured_err:
                        tail_err = "\n".join(captured_err.splitlines()[-10:])
                        tqdm.write(f"[CAPTURED STDERR — last lines]\n{tail_err}")
                # continue to next date
            finally:
                pbar.update(1)

    tqdm.write(f"\nScraping finished. Total collected products: {len(results)}")
    return results

if __name__ == "__main__":
    dates = build_dates(start_year=2013, end_year=2013)
    results = scrape_dates(dates)
    # optionally save or process results