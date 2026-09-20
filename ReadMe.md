<div align="center">

<img src="./assets/terminal-hero.gif" width="100%" alt="Jonathan Farrel Emanuel terminal profile" />

<br/>

Go-first Backend Engineer · Distributed Systems · AI Systems · Trading / Web3 Infrastructure

Email ·
LinkedIn ·
GitHub

</div>

whoami

I’m Jonathan Farrel Emanuel, a Go-first Backend Engineer with 3+ years of production experience.

Backend engineering is the center of my profile. I spend most of my time thinking about APIs, data models, service boundaries, asynchronous workflows, concurrency, transactions, reliability, observability, and the things that start to matter once software runs in production instead of only on a laptop.

My main working stack is around Go, PostgreSQL, Redis, Kafka, Docker, Kubernetes, AWS/GCP, REST, GraphQL, gRPC, CI/CD, and observability tooling. I have also worked with TypeScript/React applications, Python/ML workloads, cloud infrastructure, and internal engineering platforms.

The direction I’m building toward is broader, but still connected to the same engineering foundation:

backend engineering
        ↓
distributed & event-driven systems
        ↓
real-time data infrastructure
        ↓
AI agents / ML systems
        ↓
trading & market infrastructure
        ↓
Web3 / blockchain backend systems
        ↓
deeper systems engineering

I’m not trying to collect technologies just to make a long profile. I prefer learning them through systems where they have a real job to do: a queue has to absorb bursts, a database has to preserve correctness, an API has to fail predictably, an agent needs guardrails, and a trading or blockchain pipeline has to survive retries, reconnects, duplicate events, bad data, and partial failure.

backend --core

This is the part of engineering I identify with most.

Languages          Go · Python · TypeScript / JavaScript
APIs               REST · GraphQL · gRPC
Architecture       Microservices · Modular Services · Event-Driven Systems
Data               PostgreSQL · Redis · SQL · Transactions · Indexing
Messaging          Kafka · Async Workflows · Idempotency · Retries
Cloud              AWS · GCP · Docker · Kubernetes · Terraform
Observability      OpenTelemetry · Prometheus · Grafana · Structured Logging
Engineering        Testing · CI/CD · Code Review · Production Debugging

The backend problems I enjoy are the ones that usually appear after the happy path is finished:

transaction boundaries and consistency

concurrent workers and race conditions

duplicate messages and idempotency

retries, timeouts, backpressure, and partial failure

schema evolution and query performance

caching and invalidation

service-to-service communication

tracing, metrics, logs, and incident debugging

keeping systems understandable while they grow

That is also why Go remains my main language. It fits the kind of software I want to keep building: network services, concurrent workers, streaming systems, infrastructure, real-time data pipelines, and high-throughput backend components.

system.pipeline --live

<div align="center">

<img src="./assets/system-pipeline.gif" width="100%" alt="Animated backend pipeline" />

</div>

A common pattern I keep returning to is simple in concept:

ingest → stream → process → store → serve → observe

The hard part is making each stage reliable enough that the whole pipeline still behaves correctly when dependencies slow down, messages arrive twice, connections disappear, or traffic spikes unexpectedly.

stack --engineering-surface

<div align="center">

<img src="./assets/stack-console.gif" width="100%" alt="Animated engineering stack console" />

</div>

Current core

Backend / data / platform

Go
PostgreSQL
Redis
Kafka
REST / GraphQL / gRPC
Docker
Kubernetes
AWS / GCP
Terraform
Linux
OpenTelemetry / Prometheus / Grafana

Full-stack capability

Backend is my primary identity, but I also want enough product-side depth to own a system end to end when needed.

TypeScript
JavaScript
React
Node.js
Flutter / Dart

I’m building stronger project-level depth in:

Next.js
SvelteKit
NestJS
Express

The goal is not to become “everything at once.” The goal is to be the backend engineer who can also understand, integrate, debug, and ship the rest of the product surface.

Systems / language expansion

I’m also building deeper familiarity with:

Rust
C++
Java
Kotlin
PHP

These are expansion areas, not a claim that I have equal production depth in every language. I want each one to earn its place through a serious repository or contribution.

ai --systems-not-demos

My interest in AI is infrastructure-oriented.

I’m much more interested in how AI systems are built and operated than in wrapping a model with a single prompt.

data ingestion
    ↓
retrieval / context
    ↓
agent or model
    ↓
tools / external APIs
    ↓
validation & guardrails
    ↓
structured output
    ↓
evaluation / observability

Areas I’m actively building around:

AI agents and tool-using workflows

RAG and internal knowledge systems

research automation

model and inference pipelines

real-time computer vision

vector search

human-in-the-loop validation

evaluation and observability for AI workflows

For AI-oriented storage, I prefer starting with the simplest data layer that fits the problem:

PostgreSQL + pgvector
Redis
Supabase

and moving to dedicated vector infrastructure such as Qdrant, Weaviate, or Pinecone only when the project actually benefits from it.

trading-web3 --backend-first

I’m approaching trading and Web3 from the backend and infrastructure side.

I want to build systems such as:

Market Data
├── exchange WebSockets
├── normalization
├── order-book / trade streams
├── Kafka / streaming
├── time-series storage
└── real-time APIs

Trading Research
├── historical data
├── backtesting
├── risk engine
├── AI research agents
├── paper execution
└── monitoring

Web3 Infrastructure
├── Ethereum / EVM RPC
├── Solana data pipelines
├── wallet / ledger services
├── chain indexing
├── confirmation tracking
├── reorg / retry handling
└── on-chain analytics

This is a natural extension of backend engineering because the core problems are familiar:

concurrency, queues, transactions, idempotency, data integrity, low-latency paths, observability, and failure recovery.

Technologies I plan to use where they make sense include:

Go
PostgreSQL / TimescaleDB
Redis
Kafka / Redpanda
Ethereum tooling
Solidity
Solana tooling
Rust

My goal is to have actual portfolio systems behind those words, not just badges.

systems --next-frontier

Long term, I’m also interested in software that interacts with physical systems: telemetry, robotics, embedded or edge workloads, high-performance networking, and control-oriented software.

I do not claim aerospace, automotive-control, or robotics production experience today.

What I am building toward is the engineering base those domains require:

Go / Rust / C++
Linux
networking
concurrency
telemetry
real-time data
performance profiling
fault tolerance
hardware-adjacent systems

That is the bridge I want to build before moving into more serious machine, robotics, automotive, or aerospace software.

selected-work

observe-system

Go · observability · backend systems

A production-style backend project focused on service health, traces, metrics, logs, and operational investigation.

RevAuto

TypeScript · product engineering · full-stack

A real product-oriented codebase where I can work across application structure, business workflows, testing, and end-to-end product ownership.

blockchain-money-transfer

Go · transaction workflows · blockchain concepts

An earlier Go backend project that I plan to evolve toward stronger wallet, ledger, transaction-state, concurrency, and reliability patterns.

VisionLab

Python · computer vision · ML

Applied ML experimentation around model development, inference, and real-time processing.

next --flagship-projects

These are the projects I want to turn into the main proof-of-work on this profile:

marketstream-go
  real-time market data
  Go · Kafka · TimescaleDB · Redis · OpenTelemetry

chain-indexer-go
  blockchain indexing
  Go · EVM/Solana data · retries · confirmation/reorg handling

agentic-trading-lab
  full-stack trading research platform
  Go backend · SvelteKit · TypeScript · Python agents · backtesting

wallet-ledger-go
  transaction and wallet infrastructure
  Go · PostgreSQL · atomic transfers · idempotency · audit trail

ai-model-lab
  model engineering
  PyTorch · training → evaluation → serving · inference optimization

systems-performance-lab
  lower-level engineering
  Go · Rust · C++ · networking · concurrency · benchmarks

Every flagship repository should eventually include more than source code:

README with real architecture
architecture / ADR docs
unit + integration tests
CI
local reproducible setup
observability
security notes
benchmarks or load tests where relevant
trade-off explanations
screenshots / demo when useful

That is the standard I want the public portfolio to move toward.

principles

correctness      > cleverness
observability    > guessing
measured scaling > premature complexity
failure handling > happy-path demos
tests            > assumptions
ownership        > hand-offs
shipping         > endless planning

I like systems that stay understandable when things go wrong: a consumer lags, a transaction retries, an API dependency times out, a database slows down, or a production incident starts at an inconvenient hour.

profile-direction

The short version:

Backend first. Go at the core. Distributed systems as the foundation. AI, trading infrastructure, and Web3 as the next layer.

The broader goal is to become the kind of engineer who can move comfortably between backend services, data infrastructure, full-stack product work, intelligent systems, and deeper systems engineering without losing the production mindset that ties them together.

<div align="center">

<img src="./assets/code-rain.gif" width="100%" alt="Backend engineering code animation" />

<br/><br/>

BUILD · DEBUG · OBSERVE · OPTIMIZE · SHIP

<br/><br/>

Email ·
LinkedIn ·
GitHub

</div>
