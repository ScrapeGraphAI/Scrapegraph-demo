# 🕷️ ScrapeGraphAI: You Only Scrape Once

ScrapeGraphAI is a *web scraping* python library based on LangChain which uses LLM and direct graph logic to create scraping pipelines.
Just say which information you want to extract and the library will do it for you!

<p align="center">
  <img src="https://github.com/VinciGit00/Scrapegraph-LabLabAI-Hackathon/blob/main/docs/scrapegraphai_logo.png" alt="Scrapegraph-ai Logo" style="width: 30%;">
</p>

## 🔗 ScrapeGraph API & SDKs
If you are looking for a quick solution to integrate ScrapeGraph in your system, check out our powerful API [here!](https://dashboard.scrapegraphai.com/login)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=api_banner&utm_content=api_banner_image)
We offer SDKs in both Python and Node.js, making it easy to integrate into your projects. Check them out below:

| SDK       | Language | GitHub Link                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://github.com/ScrapeGraphAI/scrapegraph-py) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://github.com/ScrapeGraphAI/scrapegraph-js) |

## Official Demo for the ScrapeGraphAI Python SDK
This repo is a Streamlit demo for the official [`scrapegraph-py`](https://github.com/ScrapeGraphAI/scrapegraph-py) SDK.
The main page (`main.py`) calls the [ScrapeGraphAI API](https://scrapegraphai.com) through the SDK and showcases three services:

- **Extract** — AI-structured data from a URL via a natural-language prompt (with an optional JSON schema)
- **Scrape** — clean `markdown`, `html`, `links`, `images` or `summary` for a page
- **Search** — search the web and optionally extract structured data from the results

Grab an API key from the [dashboard](https://dashboard.scrapegraphai.com), paste it into the app, and run.
See [`scrapegraph_py_example.py`](scrapegraph_py_example.py) for a minimal standalone SDK script.

Link of the developed library for the hackathon Github repo:

[![My Skills](https://skillicons.dev/icons?i=github)](https://github.com/VinciGit00/Scrapegraph-ai)

Official streamlit demo:

[![My Skills](https://skillicons.dev/icons?i=react)](https://scrapegraph-demo-demo.streamlit.app)

## Example of output with TruLens
<p align="center">
  <img src="https://github.com/VinciGit00/Scrapegraph-LabLabAI-Hackathon/blob/main/assets/Trulens.png" alt="Scrapegraph-ai Logo" style="width: 60%;">
</p>

## Local execution
Is it possible to run in local this project using python with the command on your terminal with:


```bash
streamlit run main.py
```

## 🤝 Contributing

Scrapegraph-ai is [MIT LICENSED](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/LICENSE).

Contributions are welcome! Please check out the todos below, and feel free to open a pull request.

For more information, please see the [contributing guidelines](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/CONTRIBUTING.md).

Join our Discord server to discuss with us improvements and give us suggestions!

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/gkxQDAjfeX)

You can also follow all the updates on linkedin!

[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/scrapegraphai/)


## Contributors
[![Contributors](https://contrib.rocks/image?repo=VinciGit00/Scrapegraph-ai)](https://github.com/VinciGit00/Scrapegraph-ai/graphs/contributors)

## Authors

<p align="center">
  <img src="https://github.com/VinciGit00/Scrapegraph-LabLabAI-Hackathon/blob/main/docs/logo_authors.png" alt="Authors Logos">
</p>

|                    | Contact Info         |
|--------------------|----------------------|
| Marco Vinciguerra  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| Marco Perini       | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/perinim/)   |
| Lorenzo Padoan     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## Acknowledgements

- We would like to thank all the contributors to the project and the open-source community for their support.
- ScrapeGraphAI is meant to be used for data exploration and research purposes only. We are not responsible for any misuse of the library.
