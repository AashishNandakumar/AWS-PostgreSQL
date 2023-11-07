# PG-Adaptor for PIB Data Processing

The PG-Adaptor package is a collection of tools designed to manage and automate the data handling process for the Press Information Bureau (PIB) feedback system. It is structured into modules corresponding to specific roles including data harvesting, data processing, and alert dispatching.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- PostgreSQL
- Psycopg2
- Python-dotenv

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/PG-Adaptor.git
cd PG-Adaptor
```

2. **Environment Configuration**

    Create or use a .env file in the root of your project directory and add your database credentials and other configuration settings:

```bash
HOSTNAME1=your_database_host
PORT=your_database_port
USERNAME1=your_database_username
PASSWORD=your_database_password
DATABASE=your_database_name
```

### Installation

The package contains several modules, each with functions related to specific roles:
- `data_harvesters.py`: Functions to insert raw data into the source schema.
- `data_alchemists.py`: Functions to insert processed data into the processed_and_analyzed schema.
- `alert_dispatchers.py`: Functions to manage notifications in the Notification schema.

**Examples**

  To use a function from the `data_harvesters` module:

  ```python
  from pg_adaptor.data_harvesters import insert_website_data

  # Example data to insert
  data = [
      ('http://example.com', '<html>...</html>', 'English'),
      # ... more data
  ]
  
  insert_website_data(data)

  ```

### Contributing
Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your fork.

5. Create a pull request to the main repository.

Please make sure to follow the code of conduct and contribution guidelines.

### Contact
If you have any questions, suggestions, or feedback, please don't hesitate to contact us at [aashishnkumar@gmail.com]().

  
### License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/AashishNandakumar/Power-Transfer-Optimization/blob/main/LICENSE) file for details.
