import re


UNIVERSITY_RANKINGS_URL = (
    "https://www.unirank.org/kr/ranking/"
)


def current_university_ranking_response(question):
    """Return a current Korean university ranking resource when requested."""
    if not re.search(
        r"\b(?:rank|ranks|ranked|ranking|rankings)\b|ශ්‍රේණිගත",
        question or "",
        flags=re.IGNORECASE,
    ):
        return None

    link = (
        f"[Top Universities in Korea | 2026 University Ranking]"
        f"({UNIVERSITY_RANKINGS_URL})"
    )
    if re.search(r"[\u0D80-\u0DFF]", question or ""):
        answer = (
            f"දකුණු කොරියාවේ විශ්වවිද්‍යාල ranking සඳහා "
            f"{link} බලන්න. Ranking ක්‍රමවේදය සහ වර්ෂය අනුව "
            "ප්‍රතිඵල වෙනස් විය හැකි නිසා, විශ්වවිද්‍යාල සසඳන විට "
            "එම තොරතුරුත් පරීක්ෂා කරන්න."
        )
    else:
        answer = (
            f"For South Korean university rankings, see {link}. "
            "Rankings vary by publisher and methodology, so check the "
            "ranking year and criteria when comparing universities."
        )
    return {"answer": answer, "sources": []}
