# Travel Data API Service (WIP)

## Overview

This project aims to develop a RESTful API service that aggregates various travel-related signals and transforms them into a unified format. The service allows travel platforms to retrieve all relevant data in a single request, simplifying the integration process and ensuring that they have access to comprehensive datasets.

The service is designed to support batch ETL processes, rather than real-time streaming, as latency is not a concern for this particular use case. The goal is to leverage as many serverless technologies as possible, minimizing operational overhead and making the service easily scalable in the future. This project explores the implementation of the service using AWS.

## System Diagram
### AWS Version
![image](https://github.com/user-attachments/assets/6fd7fcad-aca8-48eb-9472-4033e930ef9a)


## Key Features

- **RESTful API**: A unified API endpoint that provides access to aggregated and transformed travel-related data.
- **Batch ETL Process**: Efficient batch processing to extract, transform, and load data, ensuring travel platforms receive complete data sets.
- **Serverless Architecture**: Utilizes serverless technologies to reduce infrastructure management, optimize costs, and allow for easy scalability.
- **Caching Layer**: Implements an in-memory cache to speed up data retrieval and reduce load on the underlying database.
- **Failure Handling with Kafka**: Integrates a Kafka-based message queue to ensure data is reliably processed and can be recovered in case of any failures during the ETL process.

## Technologies Used

### AWS
- **Lambda**: Serverless compute service for running the ETL process.
- **Glue**: Managed ETL service for data transformation and processing.
- **RDS**: Managed relational database service for storing transformed data.
- **ElastiCache for Redis**: In-memory caching service to accelerate data retrieval.
- **S3**: Scalable storage service for data.
- **API Gateway**: Provides secure and scalable access to the RESTful API.
- **Amazon Managed Streaming for Apache Kafka (MSK)**: Managed Kafka service for handling data ingestion and ensuring reliability in case of failures.


## Future Directions

This project serves as a foundation for further development, with the potential to scale up as the volume of data and complexity of travel-related signals increase. As the service evolves, additional features and optimizations may be implemented to enhance its functionality and performance.





