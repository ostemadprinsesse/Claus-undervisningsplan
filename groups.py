GROUP_REPOS = [
        {
            "name": "Example Group",
            "gitLinks": ["https://<git_link>"],
            "backend": "http(s)://<IP_DOMAIN>/<APIURL>",
            "frontend": "http(s)://<IP_DOMAIN>/<FrontEndURL>",
            "monitoring": "http(s)://<IP_DOMAIN>/<MonitoringURL>",
            "stack": ["Flask", "Svelte", "CouchDB", "Redis"],
            "documentation": ["link to documentation", "another link if it applies", "et cetera"],
            "members": ["Claus Bove", "Anna Alma", "Jesper Dengsø"],
        },
        {
            "name": "DenDanskeMetode",
            "gitLinks": ["https://github.com/DenDanskeMetode/legacyProject"],
            "backend": "http://131.163.89.207/api",
            "frontend": "http://131.163.89.207/",
            "monitoring": "",
            "stack": [],
            "documentation": ["http://131.163.89.207/swagger"],
            "members": ["Felix Llambias", "Nicholas Ladik", "Christian Skovgaard", "Victor Lotz"],
        },
]
