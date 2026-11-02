from types import SimpleNamespace

from app.ask import ask


class FakeResponse:
    def __init__(self, text="回答", prompt_tokens=42, output_tokens=7):
        self.text = text
        self.usage_metadata = SimpleNamespace(
            prompt_token_count=prompt_tokens,
            candidates_token_count=output_tokens,
        )


class FakeClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.models = SimpleNamespace(
            generate_content=lambda model, contents: FakeResponse()
        )


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    monkeypatch.setattr("app.ask.get_api_key", lambda: "dummy-key")
    monkeypatch.setattr("app.ask.genai.Client", FakeClient)

    result = ask("質問")

    captured = capsys.readouterr()
    assert result == "回答"
    assert "[input_tokens] 42" in captured.out
    assert "[output_tokens] 7" in captured.out


def test_ask_prints_response_latency(monkeypatch, capsys):
    monkeypatch.setattr("app.ask.get_api_key", lambda: "dummy-key")
    monkeypatch.setattr("app.ask.genai.Client", FakeClient)
    times = iter([100.0, 100.812])
    monkeypatch.setattr("app.ask.time.perf_counter", lambda: next(times))

    ask("質問")

    captured = capsys.readouterr()
    assert "[latency_ms] 812" in captured.out
