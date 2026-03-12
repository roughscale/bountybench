from resources.model_resource.model_mapping import get_model_info
from resources.model_resource.services.service_providers import ServiceProvider


def test_non_helm_gpt5_model_registered():
    model_info = get_model_info("openai/gpt-5-2025-08-07", helm=False)

    assert model_info.model_name == "gpt-5-2025-08-07"
    assert model_info.provider == ServiceProvider.OPENAI


def test_non_helm_claude_sonnet_4_model_registered():
    model_info = get_model_info("anthropic/claude-sonnet-4-5-20250929", helm=False)

    assert model_info.model_name == "claude-sonnet-4-5-20250929"
    assert model_info.provider == ServiceProvider.ANTHROPIC
