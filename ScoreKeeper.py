class ScoreKeeper:
    """
    Class devoted to keeping score for Anagram Hunt and Math Facts.
    """
    count = 0
    @classmethod
    def increment_count(cls):
        "Increment score by one when user has correct answer"
        cls.count += 1
        return cls.count
