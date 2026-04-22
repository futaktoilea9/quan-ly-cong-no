from pathlib import Path


def test_finance_project_has_docs_and_runtime_ignore():
    assert Path('docs/product-overview.md').exists()
    assert 'app.db' in Path('.gitignore').read_text(encoding='utf-8')
