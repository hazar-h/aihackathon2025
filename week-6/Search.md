# Search Techniques — Comparative Reference

This document provides a practical overview of common search data management approaches: **SQL**, **NoSQL**, **Elasticsearch**, and **Vector Databases**.  
It outlines when each approach is appropriate, how they differ in behavior and data handling, and which algorithms or design principles are typically involved.

---

## 1. SQL-Based Search (Relational Databases)

### Overview
SQL databases (such as **PostgreSQL**, **MySQL**, **MariaDB**, **SQLite**) use a **relational data model** with structured schemas.  
Search operations are performed using SQL queries and are most effective for **structured data with defined relationships**.

### When to Use
- Data has a clear, rigid schema (tables, columns, foreign keys).  
- Consistency and integrity (ACID compliance) are required.  
- Queries are deterministic, transactional, or require aggregation and joins.  
- Text search needs are simple or moderately complex.

### Typical Scenarios
- Financial and inventory systems  
- Administrative dashboards and reports  
- Applications where relationships between entities are critical  
- Structured metadata search (e.g., filtering records by attributes)

### Relevant Techniques
- **Full-Text Search (FTS)** in PostgreSQL using `tsvector` and `tsquery`  
- **GIN/GiST indexes** for fast text or range queries  
- **Trigram similarity** (`pg_trgm` extension) for approximate string matching  
- **Materialized views** to cache and pre-rank frequently queried data

### Limitations
- Not optimized for large-scale text search or unstructured data.  
- Limited ranking and fuzzy matching capabilities.  
- Vertical scaling typically required for performance.

---

## 2. NoSQL Search (Document and Key-Value Databases)

### Overview
NoSQL databases (e.g., **MongoDB**, **Couchbase**, **DynamoDB**) store data in **schema-flexible formats** such as JSON documents or key-value pairs.  
Search capabilities vary depending on the type of store but are generally suited for semi-structured data.

### When to Use
- Data structure varies frequently between records.  
- Scalability, flexibility, and horizontal partitioning are priorities.  
- Simple key-based lookups, range queries, or filters dominate.  
- Text search requirements are moderate, not full enterprise-grade.

### Typical Scenarios
- Product catalogs and user profile storage  
- Log and event capture systems  
- Mobile or IoT applications where data shape evolves over time

### Relevant Techniques
- **MongoDB Atlas Search** (Lucene-based full-text search engine)  
- **Prefix and range queries** on indexed fields  
- **Aggregation pipelines** for filtering and scoring  
- **Denormalization** to improve read performance (data embedding)

### Limitations
- Joins and relational queries are limited or simulated via aggregation.  
- Search performance depends heavily on indexing strategy.  
- Full-text capabilities less mature than Elasticsearch.

---

## 3. Elasticsearch (Full-Text and Relevance-Oriented Search)

### Overview
**Elasticsearch** is a distributed search and analytics engine based on **Lucene**.  
It is designed for large-scale **full-text search**, **log analytics**, and **relevance-based document retrieval**.

### When to Use
- Data is text-heavy or unstructured (articles, logs, documents).  
- Search relevance and ranking are important.  
- Users need partial matches, fuzzy search, or synonym handling.  
- Query volume is high and requires fast response times.

### Typical Scenarios
- E-commerce product or catalog search  
- Website or application search functionality  
- Centralized log management and analytics (ELK stack)  
- Document indexing for content platforms

### Relevant Techniques
- **BM25 ranking algorithm** for relevance scoring  
- **Tokenization and analyzers** for language processing (stemming, stopwords)  
- **Synonym filters** for more inclusive matching  
- **Fuzzy and wildcard queries** for typo-tolerant search  
- **Faceted search**, **autocomplete**, and **highlighting** for UX improvements  
- Can be extended with **vector search plugins** for hybrid scoring

### Limitations
- Requires cluster management and indexing overhead.  
- Consumes significant memory and disk for large indices.  
- Writes are slower than reads due to index rebuilding.

---

## 4. Vector Databases (Semantic and Similarity Search)

### Overview
Vector databases (e.g., **Qdrant**, **Milvus**, **Weaviate**, **FAISS**) store data as **vectors (numerical embeddings)** in high-dimensional space.  
Search is performed by comparing vectors using mathematical similarity measures.

### When to Use
- Search is based on **meaning, context, or similarity**, not literal text.  
- Data includes **unstructured content** (documents, code, images, etc.).  
- You require **nearest-neighbor retrieval** by similarity score.  
- Keyword search is insufficient for identifying related or equivalent items.

### Typical Scenarios
- Document retrieval by content or context  
- Image, audio, or media similarity search  
- Knowledge management systems and question-answer retrieval  
- Hybrid search in combination with keyword-based systems

### Relevant Techniques
- **Approximate Nearest Neighbor (ANN)** search for high performance  
- **Cosine similarity**, **dot product**, or **Euclidean distance** as ranking metrics  
- **Vector normalization** for consistent scoring  
- **Hybrid search** (combine lexical search + vector similarity)  
- **Reranking** for refining top results (see section below)

### Limitations
- Requires vector generation (embeddings) via preprocessing.  
- Performance and accuracy depend on vector dimensionality and algorithm tuning.  
- Primarily suited for retrieval tasks, not transactional systems.

---

## 5. Reranking and Relevance Optimization

Reranking techniques reorder search results to improve precision and relevance.  
This step is typically applied **after** an initial retrieval (e.g., top-k results).

### Common Techniques

| Algorithm | Description | Common Usage |
|------------|--------------|--------------|
| **BM25** | Probabilistic ranking based on term frequency and inverse document frequency | Text search engines (e.g., Elasticsearch, PostgreSQL FTS) |
| **TF-IDF** | Traditional term-weighting method, precursor to BM25 | Academic and small-scale systems |
| **Cosine Similarity** | Measures angular distance between vectors | Vector-based retrieval |
| **Hybrid Scoring** | Combines keyword ranking (BM25) and vector similarity | Mixed data search |
| **Cross-Reranking** | Re-evaluates top results using more detailed features | High-precision retrieval |

### Typical Pipeline
1. Retrieve candidate results (using SQL, Elasticsearch, or Vector DB).  
2. Compute relevance scores for each candidate.  
3. Reorder based on combined score (lexical + similarity).  
4. Return final ranked list.

---

## 6. Comparison Summary

| Property | SQL | NoSQL | Elasticsearch | Vector Database |
|-----------|------|--------|---------------|----------------|
| **Data Model** | Relational | Document / Key-Value | Document-Oriented | High-Dimensional Vector |
| **Schema** | Strict | Flexible | Semi-Structured | N/A |
| **Query Type** | Structured / Deterministic | Lookup / Aggregation | Full-Text / Fuzzy | Similarity |
| **Ranking** | Deterministic | Basic | Statistical (BM25) | Geometric (Distance) |
| **Scalability** | Vertical | Horizontal | Horizontal | Horizontal |
| **Transaction Support** | Strong (ACID) | Variable | Weak | None |
| **Ideal Use Case** | Analytics, relational data | Flexible documents | Text search and logs | Contextual similarity |
| **Examples** | PostgreSQL, MySQL | MongoDB, DynamoDB | Elasticsearch, OpenSearch | Qdrant, Weaviate, Milvus |

---

## 7. Combining Systems

In practice, many production systems use **multiple search technologies** together:

- **SQL + Elasticsearch**: transactional integrity + full-text search  
- **NoSQL + Elasticsearch**: scalable storage + text indexing  
- **Elasticsearch + Vector Database**: hybrid search (keyword + semantic similarity)  
- **SQL + Vector Indexing**: structured filters + contextual ranking

---

## 8. Decision Guide

| Scenario | Recommended Approach |
|-----------|----------------------|
| Structured records with strict schema | SQL |
| JSON documents or frequently changing schema | NoSQL |
| Large-scale text search with ranking | Elasticsearch |
| Search by meaning or context | Vector Database |
| Combine textual and contextual retrieval | Hybrid (Elasticsearch + Vector DB) |

---

## 9. Summary

Each search system excels under different constraints:

- **SQL**: precise, transactional, structured  
- **NoSQL**: flexible, scalable, schema-light  
- **Elasticsearch**: text-optimized, relevance-driven  
- **Vector Databases**: similarity-based, context-aware  

A well-architected application selects or combines these systems based on **data type**, **query intent**, and **performance requirements**.
