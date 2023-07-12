# Website Blocker Script

This Python script allows you to block access to specific websites on your local computer running Windows. It works by modifying the `hosts` file on the computer to redirect any requests to the blocked websites to the local IP address.

### Installation

To use this script, you need to have Python installed on your computer. You can download and install Python from the official website (https://www.python.org/downloads/).

### Usage

1. Open the script in a text editor or Python IDE.

2. Modify the `website_list` variable to include the list of websites that you want to block.

3. Modify the `hosts_paths` variable to point to the location of the `hosts` file on your computer. By default, it is located at `C:\Windows\System32\drivers\etc\hosts`.

4. Run the script using the command `python website_blocker.py` in the command prompt.

5. The script will run continuously in the background and block access to the specified websites during working hours (defined in the `if` statement). Outside of working hours, the script will unblock access to the websites.

### Customization

You can customize this script by modifying the following variables:

- `hosts_paths`: The path to the `hosts` file on your computer.
- `website_list`: The list of websites that you want to block.
- `redirect`: The IP address that you want to redirect requests to (default is `127.0.0.1`).

You can also modify the working hours by changing the values in the `dt` function.

### Conclusion

That's it! You now have a simple Python script that can block access to specific websites on your local computer running Windows. Feel free to customize it further to suit your needs.
