# BizCard-API

I biglietti da visita di carta si piegano, si perdono nel portafoglio e finiscono in lavatrice. Le API no.

Questo è il mio biglietto da visita digitale. Niente frontend complesso, solo un'interfaccia pulita che ti risponde in JSON.

![Build and Push Docker Image](https://github.com/pzzt/bizcard-api/actions/workflows/docker-publish.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/pzzt/bizcard-api)

### Come si usa?

Niente installazioni, niente "sulla mia macchina funziona". Io ho impacchettato tutto, tu devi solo scaricarlo.

Apri il terminale e lancia:

```bash
docker run -p 8000:8000 pzzt/bizcard-api:latest
```

Poi apri il browser su [http://localhost:8000/](http://localhost:8000/)

### Il trucco dietro il sipario

Sotto questa facciata da semplice biglietto da visita si nasconde un piccolo robot.
Ogni volta che cambio una virgola nel mio biglietto da visita e faccio un `git push`, un'automazione prende il codice, lo chiude in un container Docker perfettamente pulito e lo consegna da sola sugli scaffali di Docker Hub. Zero sforzi manuali, zero errori umani.

### Cosa trovi dentro?

* `GET /`
* `GET /skills`
* `GET /contatti`

### Test da terminale

~~~bash
# Messaggio di benvenuto
curl -s http://localhost:8000/ | python -m json.tool

# Le competenze
curl -s http://localhost:8000/skills | python -m json.tool

# I contatti
curl -s http://localhost:8000/contatti | python -m json.tool
~~~
