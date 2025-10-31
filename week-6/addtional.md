## Wide-Column Databases

### Overview

Wide-column databases (e.g., **Apache Cassandra**, **ScyllaDB**, **HBase**) organize data into **tables, rows, and dynamic columns**, but unlike traditional relational systems, each row can contain a **different set of columns**.
They are designed for **large-scale, high-throughput workloads** and **distributed storage** across multiple nodes.

### When to Use

* You need **massive write scalability** and **low-latency reads**.
* The dataset is **large and sparse**, often time-based or event-driven.
* The schema can vary across records, but consistent access patterns are known.
* You require **horizontal scaling** across commodity servers.

### Typical Scenarios

* IoT telemetry and sensor data collection
* Event logging and analytics at scale
* Messaging systems or user activity tracking
* Applications requiring predictable query access patterns

### Relevant Techniques

* **Partition keys** and **clustering keys** to define data distribution
* **Tunable consistency levels** (per query) to balance performance vs. accuracy
* **Compaction strategies** for optimizing storage
* **Secondary indexes** for limited non-key lookups

### Limitations

* Requires careful schema design; query patterns must be known in advance.
* Limited ad-hoc querying and joins.
* No native full-text or complex relational querying.

---

## Time-Series Databases

### Overview

Time-series databases (TSDBs) such as **InfluxDB**, **TimescaleDB**, **QuestDB**, or **Prometheus** are optimized for storing and querying **timestamped data**.
They specialize in handling **high-frequency inserts**, **data retention**, and **time-based aggregations**.

### When to Use

* Data consists of **metrics, events, or measurements** over time.
* Queries frequently involve **aggregations**, **downsampling**, or **time windows**.
* Performance and compression efficiency for **append-only** data are important.
* You require **continuous ingestion** and periodic **data expiration**.

### Typical Scenarios

* Application, system, or infrastructure monitoring
* IoT and sensor data analysis
* Financial market tick data
* Real-time analytics dashboards

### Relevant Techniques

* **Retention policies** and **continuous queries** for auto-aggregation
* **Compression and chunking** for high ingestion performance
* **Downsampling** to manage data growth over time
* Integration with **Grafana** or **Kibana** for visualization

### Limitations

* Not suited for arbitrary relational joins or text queries.
* Query performance can degrade if time indexes are mismanaged.
* Write-heavy workloads require tuned storage and retention policies.

---

## Graph Databases

### Overview

Graph databases (e.g., **Neo4j**, **Amazon Neptune**, **ArangoDB**, **JanusGraph**) store data as **nodes (entities)** and **edges (relationships)**.
They are optimized for **relationship-centric queries** and **network traversal operations**.

### When to Use

* Data is naturally relational and interconnected.
* You need to model **networks, hierarchies, or dependencies**.
* Queries involve **pathfinding**, **recommendations**, or **graph traversal**.
* Schema flexibility is desired with fast access to connected data.

### Typical Scenarios

* Social networks and recommendation systems
* Fraud detection and risk analysis
* Knowledge graphs and dependency graphs
* Network topology and asset mapping

### Relevant Techniques

* **Property graph model** (nodes and edges with attributes)
* Query languages like **Cypher** (Neo4j) or **Gremlin** (Apache TinkerPop)
* **Graph traversal algorithms** (shortest path, PageRank, centrality)
* **Hybrid integration** with relational or search databases for enriched queries

### Limitations

* Not ideal for bulk analytical queries or large-scale text searches.
* Graph traversal performance depends on indexing and graph structure.
* Scaling horizontally can be complex compared to document or key-value stores.

---