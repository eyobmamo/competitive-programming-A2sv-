class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.time = defaultdict(set)
        self.token = {}

    def delete_old_tokens(self, currentTime):
        delete = []
        for expiry, tokens in self.time.items():
            if expiry > currentTime:
                break
            delete.append(expiry)
        
        for expiry in delete:
            for tokenId in self.time[expiry]:
                del self.token[tokenId]
            del self.time[expiry]

    def generate(self, tokenId: str, currentTime: int) -> None:
        new_expiry = currentTime + self.ttl
        self.token[tokenId] = new_expiry
        self.time[new_expiry].add(tokenId)

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.delete_old_tokens(currentTime)
        if tokenId not in self.token: return

        expiry = self.token[tokenId]
        self.time[expiry].remove(tokenId)
        new_expiry = currentTime + self.ttl
        self.token[tokenId] = new_expiry
        self.time[new_expiry].add(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.delete_old_tokens(currentTime)
        return len(self.token)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)