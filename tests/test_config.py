"""
test_config.py - Validate mkdocs.yml and project structure for G_TrakCare_Explorer.

Ensures the MkDocs configuration is valid YAML and contains the required keys
for building the documentation site.
"""

import os
import pytest

yaml = pytest.importorskip("yaml")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestMkdocsConfig:
    """Validate mkdocs.yml structure and content."""

    @pytest.fixture(autouse=True)
    def load_config(self):
        config_path = os.path.join(PROJECT_ROOT, "mkdocs.yml")
        assert os.path.exists(config_path), "mkdocs.yml must exist"
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    def test_config_is_dict(self):
        assert isinstance(self.config, dict)

    def test_site_name_defined(self):
        assert "site_name" in self.config
        assert isinstance(self.config["site_name"], str)
        assert len(self.config["site_name"]) > 0

    def test_docs_dir_defined(self):
        assert "docs_dir" in self.config

    def test_docs_dir_exists_on_disk(self):
        docs_dir = self.config.get("docs_dir", "docs")
        docs_path = os.path.join(PROJECT_ROOT, docs_dir)
        assert os.path.isdir(docs_path), f"docs_dir '{docs_dir}' must exist: {docs_path}"

    def test_site_dir_defined(self):
        assert "site_dir" in self.config

    def test_theme_defined(self):
        assert "theme" in self.config
        assert isinstance(self.config["theme"], dict)

    def test_theme_name_is_material(self):
        assert self.config["theme"]["name"] == "material"

    def test_theme_language_is_es(self):
        assert self.config["theme"]["language"] == "es"

    def test_nav_defined(self):
        assert "nav" in self.config
        assert isinstance(self.config["nav"], list)
        assert len(self.config["nav"]) > 0

    def test_plugins_include_search(self):
        assert "plugins" in self.config
        assert "search" in self.config["plugins"]

    def test_markdown_extensions_defined(self):
        assert "markdown_extensions" in self.config
        extensions = self.config["markdown_extensions"]
        assert isinstance(extensions, list)
        assert len(extensions) > 0

    def test_admonition_extension_enabled(self):
        extensions = self.config["markdown_extensions"]
        # Extensions can be strings or dicts with config
        ext_names = []
        for ext in extensions:
            if isinstance(ext, str):
                ext_names.append(ext)
            elif isinstance(ext, dict):
                ext_names.extend(ext.keys())
        assert "admonition" in ext_names


class TestNavReferencedFilesExist:
    """Check that files referenced in the nav section actually exist."""

    @pytest.fixture(autouse=True)
    def setup(self):
        config_path = os.path.join(PROJECT_ROOT, "mkdocs.yml")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        self.docs_dir = os.path.join(PROJECT_ROOT, self.config.get("docs_dir", "docs"))

    def _extract_paths(self, nav_items):
        """Recursively extract file paths from nav structure."""
        paths = []
        for item in nav_items:
            if isinstance(item, str):
                paths.append(item)
            elif isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, str):
                        paths.append(value)
                    elif isinstance(value, list):
                        paths.extend(self._extract_paths(value))
                    elif isinstance(value, dict):
                        paths.extend(self._extract_paths([value]))
        return paths

    def test_nav_md_files_exist(self):
        """Every .md file referenced in nav should exist in docs_dir."""
        nav = self.config.get("nav", [])
        paths = self._extract_paths(nav)

        missing = []
        for p in paths:
            if p.endswith(".md"):
                full_path = os.path.join(self.docs_dir, p)
                if not os.path.exists(full_path):
                    missing.append(p)

        # Report all missing at once for easier debugging
        assert missing == [], f"Missing nav-referenced .md files: {missing}"


class TestProjectStructure:
    """Validate essential project files exist."""

    def test_readme_exists(self):
        assert os.path.exists(os.path.join(PROJECT_ROOT, "README.md"))

    def test_makefile_exists(self):
        assert os.path.exists(os.path.join(PROJECT_ROOT, "Makefile"))

    def test_requirements_txt_exists(self):
        assert os.path.exists(os.path.join(PROJECT_ROOT, "requirements.txt"))

    def test_wiki_docs_dir_exists(self):
        assert os.path.isdir(os.path.join(PROJECT_ROOT, "wiki", "docs"))

    def test_flujograma_dir_exists(self):
        assert os.path.isdir(os.path.join(PROJECT_ROOT, "Flujograma"))

    def test_pyproject_toml_exists(self):
        assert os.path.exists(os.path.join(PROJECT_ROOT, "pyproject.toml"))
