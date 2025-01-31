<h1 style="text-align: center;">Emigrant API</h1>
<p style="text-align: center;">Made for <a href="https://raspapi.hackclub.com">RaspAPI</a> and <a href="https://highseas.hackclub.com">High Seas</a> project !!
</p>

## About this API
This is a simple Flask-based API for getting emigrants data which is getting its source from a CSV file (Sources and credits given below)

- This API makes use of Flask and Python
- The dataset does not have each year. For more details on what are the limitations, <a href="">check here</a>
- This API does have one social feature which is commenting! You can see, send and express yourself by sending API Requests (API Endpoints given below)

## Use this API
- This API is hosted on a nest (linux) server at `http://37.27.51.34:46699/`
- The endpoints are given below.

## Endpoints
- GET `/api/v1/filter?column=<column_name>&value=<value>`
- GET `/api/v1/unique_values?column=<column_name>`
- GET `/api/v1/total_records`
- POST `/api/v1/add_comment`
- GET `/api/v1/comments`
- GET `/api/v1/comments?username=<username>`

## Dataset Columns
The dataset contains the following columns:
- `Entity`: The name of the country or region.
- `year`: The year of the data.
- `numberofemigrants`: The number of emigrants for that year and entity.

## Contributing
We welcome contributions to improve this API. Here are some ways you can contribute:
1. **Report Bugs**: If you find a bug, please report it by creating an issue.
2. **Feature Requests**: If you have an idea for a new feature, please submit a feature request.
3. **Pull Requests**: If you want to contribute code, please fork the repository and submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits
- Data Source: [Kaggle](https://kaggle.com/)
