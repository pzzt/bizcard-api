from fastapi import FastAPI

app = FastAPI(title="Andrea Pozzato", description="API Business Card", version="0.0.1")


@app.get("/")
def read_root():
    return {"message": "Ti do il benvenuto, mi chiamo Andrea Pozzato", "status": "ok"}


@app.get("/skills")
def get_skills():
    return {
        "linguaggi": ["Python", "Bash"],
        "devops": ["Docker", "GitHub Actions", "Git"],
        "frameworks": ["FastAPI", "Flask"],
        "Hypervisors": ["VMware", "Proxmox"],
    }


@app.get("/contatti")
def get_contatti():
    return {
        "github": "https://github.com/pzzt",
        "linkedin": "https://linkedin.com/in/andreapozzato",
        "website": "https://andreapozzato.com",
    }
