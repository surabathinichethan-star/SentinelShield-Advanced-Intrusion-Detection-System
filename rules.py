attack_patterns = {
    "SQL Injection": [
        "' OR '1'='1",
        "SELECT * FROM",
        "UNION SELECT"
    ],

    "XSS": [
        "<script>",
        "</script>",
        "javascript:"
    ],

    "Directory Traversal": [
        "../",
        "../../"
    ],

    "Command Injection": [
        "; ls",
        "; cat",
        "&&"
    ],

    "LFI": [
        "/etc/passwd",
        "boot.ini"
    ]
}