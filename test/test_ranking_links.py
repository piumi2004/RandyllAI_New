import unittest

from backend.ranking_links import (
    UNIVERSITY_RANKINGS_URL,
    current_university_ranking_response,
)


class UniversityRankingLinkTests(unittest.TestCase):
    def test_ranking_response_links_to_the_ranking_page(self):
        response = current_university_ranking_response(
            "What are the top university rankings in Korea?"
        )

        self.assertIn(
            f"]({UNIVERSITY_RANKINGS_URL})",
            response["answer"],
        )
        self.assertNotIn("#", UNIVERSITY_RANKINGS_URL)

    def test_non_ranking_questions_are_not_routed_to_rankings(self):
        self.assertIsNone(
            current_university_ranking_response(
                "What are the admission requirements in Korea?"
            )
        )


if __name__ == "__main__":
    unittest.main()
