class NodeMavenProxyManager:
    def __init__(self, proxies_list):
        """
        Initialize the NodeMaven Proxy Manager.

        Args:
            proxies_list (list of dict): A list of proxies, each as a dictionary 
                                         containing IP, port, username, and password.
        """
        self.proxies_list = proxies_list
        self.current_proxy = None

    def _format_proxy(self, proxy):
        """
        Format the proxy details into a string suitable for use with requests.

        Args:
            proxy (dict): Proxy configuration details.

        Returns:
            str: Formatted proxy string.
        """
        ip = proxy['ip']
        port = proxy['port']
        username = proxy['username']
        password = proxy['password']
        return f"http://{username}:{password}@{ip}:{port}"

    def select_proxy(self, index):
        """
        Select a proxy from the list based on the provided index.

        Args:
            index (int): Index of the proxy in the list.

        Returns:
            bool: True if the proxy was selected successfully, False otherwise.
        """
        try:
            self.current_proxy = self.proxies_list[index]
            return True
        except IndexError:
            print("Invalid proxy index.")
            return False

    def get_current_proxy(self):
        """
        Get the currently selected proxy.

        Returns:
            dict: Proxy configuration details.
        """
        return self.current_proxy

    def apply_proxy_to_request(self, request_session):
        """
        Apply the current proxy to a given requests session.

        Args:
            request_session (requests.Session): The session to which the proxy will be applied.

        Returns:
            None
        """
        if self.current_proxy:
            proxy_str = self._format_proxy(self.current_proxy)
            request_session.proxies.update({"http": proxy_str, "https": proxy_str})
        else:
            print("No proxy is currently selected.")

# Example Usage
if __name__ == "__main__":
    proxies = [
        {'ip': '192.168.0.1', 'port': 8080, 'username': 'user1', 'password': 'pass1'},
        {'ip': '192.168.0.2', 'port': 8081, 'username': 'user2', 'password': 'pass2'}
    ]

    proxy_manager = NodeMavenProxyManager(proxies)
    proxy_manager.select_proxy(0)
    print("Current Proxy:", proxy_manager.get_current_proxy())
# Configuration and usage of NodeMaven Proxies
