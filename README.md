
<a name="top"></a>


<h3 align="center">Data Load to Tableau Server</h3>

  <p align="center">
    This program refresh the data from local folders into Tableau server online with different options.
    <br/>
  </p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project


This project is to update or overwrite files in Tableau Online using Python. The goal is to either load a single file, or all files in a folder or combine various Excel files into a single Hyper file, and also allowing the selection of specific columns from these Excel files during the upload process. This approach is beneficial when there are restrictions on permissions to the file folder form tableau, and the automation of data refresh is desired.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* Python
* TableauServerClient
* Pantab
* Pandas

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

Below are instruction on some of the libraries that are needed before running the program.

### Prerequisites

Below are the libraries that are needed to be installed before running the program.

 ```sh
pip install tableauserverclient
pip install pantab
pip install pandas
 ```

 ### Installation

1. Install all the prerequisite libraries.
2. Download the git repo.
3. Update the params.py for details on the project.
4. Update the main.py with some of the local params of the project.


<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

Once all the installation steps are done to update the properties the program can be executed by running the main.py file.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


## License

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

Mary Myrtle Jerome - asterflorence@gmail.com

## Acknowledgments
