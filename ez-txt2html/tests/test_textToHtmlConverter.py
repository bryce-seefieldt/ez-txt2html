import os
import pytest
from unittest.mock import patch
from ..ez_txt2html import (
    ez_txt2html_main,
    textToHtmlConverter,
    fileConversion,
    openCurrentFile,
    convertTextContent,
    writeToHtmlFile,
    parseMarkdownToHtml,
)


class TestOpenCurrentFile:
    def test_read_existing_file(self, tmpdir):
        # Create a temporary file with content
        file_content = "Line 1\nLine 2\nLine 3"
        file_path = os.path.join(tmpdir, "test.txt")
        with open(file_path, "w") as test_file:
            test_file.write(file_content)
        # Call the openCurrentFile function
        parsed_lines = openCurrentFile(file_path)
        # Assert that the function correctly reads and returns the lines
        # from the file
        assert parsed_lines == ["Line 1\n", "Line 2\n", "Line 3"]

    def test_read_empty_file(self, tmpdir):
        # Create an empty temporary file
        file_path = os.path.join(tmpdir, "empty.txt")
        open(file_path, "w").close()  # Create an empty file

        # Call the openCurrentFile function
        parsed_lines = openCurrentFile(file_path)

        # Assert that the function returns an empty list for an empty file
        assert parsed_lines == []

    def test_nonexistent_file(self):
        # Call the openCurrentFile function with a nonexistent file
        with pytest.raises(FileNotFoundError):
            openCurrentFile("nonexistent_file.txt")


class TestWriteToHtmlFile:
    def test_write_content_to_file(self, tmpdir):
        # Create a temporary HTML file path
        output_path = os.path.join(tmpdir, "output.html")

        # Call the writeToHtmlFile function
        content = "<p>Test HTML content</p>"
        writeToHtmlFile(output_path, content)

        # Assert that the file has been created and contains the expected
        # content
        assert os.path.exists(output_path)
        with open(output_path, "r") as html_file:
            assert html_file.read() == content

    def test_overwrite_existing_file(self, tmpdir):
        # Create an existing HTML file
        output_path = os.path.join(tmpdir, "existing.html")
        with open(output_path, "w") as existing_file:
            existing_file.write("Existing content")

        # Call the writeToHtmlFile function to overwrite the existing file
        content = "<p>New content</p>"
        writeToHtmlFile(output_path, content)

        # Assert that the file has been overwritten and contains the new content
        with open(output_path, "r") as html_file:
            assert html_file.read() == content

    def test_empty_content(self, tmpdir):
        # Create a temporary HTML file path
        output_path = os.path.join(tmpdir, "empty.html")

        # Call the writeToHtmlFile function with empty content
        writeToHtmlFile(output_path, "")

        # Assert that the file has been created and is empty
        assert os.path.exists(output_path)
        with open(output_path, "r") as html_file:
            assert html_file.read() == ""

    def test_invalid_path(self):
        # Call the writeToHtmlFile function with an invalid path
        with pytest.raises(FileNotFoundError):
            writeToHtmlFile(
                "/invalid/path/output.html", "<p>Test HTML content</p>"
            )

    def test_invalid_content_type(self, tmpdir):
        # Create a temporary HTML file path
        output_path = os.path.join(tmpdir, "output.html")

        # Call the writeToHtmlFile function with invalid content type
        with pytest.raises(TypeError):
            writeToHtmlFile(
                output_path, 123
            )  # Passing an integer instead of a string


class TestParseMarkdownToHtml:
    def test_empty_input(self):
        # Test when the input markdownLines is empty
        assert parseMarkdownToHtml([]) == ""

    def test_basic_markdown_formatting(self):
        # Test basic markdown formatting
        markdown_lines = [
            "# Heading 1",
            "This is **bold** text",
            "This is *italic* text",
        ]
        expected_html = "<p><h1>Heading 1</h1>\nThis is <strong>bold</strong> text\nThis is <em>italic</em> text\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_code_block(self):
        # Test markdown code block formatting
        markdown_lines = ["```\nprint('Hello, World!')\n```"]
        expected_html = "<p><code>\nprint('Hello, World!')\n</code>\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_nested_markdown_formatting(self):
        # Test nested markdown formatting
        markdown_lines = [
            "## Nested Heading",
            "This is **bold and *italic* text**.",
        ]
        expected_html = "<p><h2>Nested Heading</h2>\nThis is <strong>bold and <em>italic</em> text</strong>.\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_hr_tag(self):
        # Test markdown horizontal rule formatting
        markdown_lines = ["---"]
        expected_html = "<p><hr />\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_multiple_paragraphs(self):
        # Test multiple paragraphs in the input
        markdown_lines = ["Paragraph 1", "", "Paragraph 2"]
        expected_html = "<p>Paragraph 1\n</p>\n<p>Paragraph 2\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_code_fence_toggle(self):
        # Test code fence toggle
        markdown_lines = [
            "```\nCode 1\n```",
            "Normal text",
            "```\nCode 2\n```",
        ]
        expected_html = "<p><code>\nCode 1\n</code>\nNormal text\n<code>\nCode 2\n</code>\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_unmatched_code_fence(self):
        # Test handling of unmatched code fence
        markdown_lines = ["```\nUnmatched code fence"]
        expected_html = "<p><code>\nUnmatched code fence\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_invalid_heading_format(self):
        # Test invalid heading format
        markdown_lines = ["#Invalid Heading"]
        expected_html = "<p>#Invalid Heading\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html

    def test_inline_code(self):
        # Test inline code formatting
        markdown_lines = ["This is `inline code`."]
        expected_html = "<p>This is <code>inline code</code>.\n</p>\n"
        assert parseMarkdownToHtml(markdown_lines) == expected_html


class TestPaths:
    def test_invalid_path(self, capsys):
        invalid_path = "nonexistent_path"
        output_path = "output_path"
        textToHtmlConverter(invalid_path, output_path)
        # Capture the printed output
        captured = capsys.readouterr()
        # Assert that the printed output contains the expected error message
        assert "Error: Invalid path provided" in captured.out

    # def test_no_write_permissions(self, capsys):
    #     input_path = "./examples"
    #     output_path = "c://"
    #     # Use patch to simulate a directory without write permissions
    #     with patch("os.access", return_value=False):
    #         textToHtmlConverter(input_path, output_path)
    #         captured = capsys.readouterr()
    #         assert "Error: [WinError 5] Access is denied:" in captured.out
