As we develop new features and fix bugs for Mixxx, we need feedback from users. Testing the latest developments is a great way to contribute to Mixxx.

## Backup settings and database

We try to ensure that upgrading to new versions does not interfere with settings from older versions, but we might not catch every potential issue immediately. Before switching from a stable release of Mixxx to a development version, it is recommended to make a backup copy of your settings and library database, as well as your controller mappings and track waveforms (if you chose to store them).  
You can backup all that by copying this whole folder:  

**Linux**  
`~/.mixxx/`  
Note: make sure you have 'Show hidden files' enabled in your file manager
in order to show all dot-files and folders.

**Windows**  
Vista and up: `%LOCALAPPDATA%\Mixxx\`  
XP and below: `%USERPROFILE%\Local Settings\Application Data\Mixxx\`  
Type either of those into the location bar of a Computer or Folder window.

**macOS**  
Mixxx 2.3: `~/Library/Containers/org.mixxx.mixxx/Data/Library/Application Support/Mixxx`  
Mixxx 2.2 and earlier: `~/Library/Application Support/Mixxx`  

## Main branch builds

Every time we change the code, GitHub Actions makes a build and uploads it to [https://downloads.mixxx.org/builds/main/](https://downloads.mixxx.org/builds/main/). We try to keep the main branch reasonably stable and not merge new features until we're fairly confident they are not going to create serious issues. However, if you want to perform with these, do so at your own risk. If you do decide to perform with a main branch build, test the same build for several practice sets before your gig to check that it works with your particular setup. If you encounter a bug, please [report it](reporting-bugs).

If you are using a Linux distribution other than Ubuntu or a derivative distribution that is incompatible with Ubuntu .deb packages,
you will need to [compile from source code](https://github.com/mixxxdj/mixxx/wiki/compiling-on-Linux) to test the main Git branch.

## GitHub pull requests

If you would really like to be on the bleeding edge, you can try out [pull requests on GitHub](https://github.com/mixxxdj/mixxx/pulls) before
they get merged to the main branch. This way you can be involved in the design of new features as they are being implemented. If there is an
issue with a build from a pull request, comment on the pull request on GitHub instead of opening a bug on Launchpad.

GitHub Actions automatically builds every pull request. They are not uploaded to downloads.mixxx.org, but you can access them through GitHub. If you do not have a GitHub account already, you will need to [register one](https://github.com/join) and log in to download pull request builds.

Go to the bottom of the pull request and look at the report of the builds & test results below the last comment on the page. Click "Show all checks"
![Screenshot of GitHub Actions checked on a pull request (collapsed)](https://user-images.githubusercontent.com/9455094/101260541-73f19900-36f6-11eb-8874-1375bfe4c368.png)

Where it says "Build / YOUR_OPERATING_SYSTEM", click the "Details" link.
![Screenshot of GitHub Actions checks on a pull request](https://user-images.githubusercontent.com/9455094/100259209-94a73b00-2f0d-11eb-9ec1-1bef45b1ba14.png)

On the next page, click the "Artifacts" link in the top right to show a menu of the build artifacts (assuming the builds succeeded).
![GitHub Action artifact download menu](https://user-images.githubusercontent.com/9455094/100259372-c1f3e900-2f0d-11eb-82df-6d3ecb343f19.png)

Click the link to download the build for your operating system. GitHub Actions automatically wraps the installer in a ZIP file, so you need to extract the ZIP file before running the installer.

Pull request builds are not code signed, so macOS and Windows will warn you about installing them.

To run unsigned builds on macOS, right click on the Mixxx.app file in Finder and select "Open". macOS will warn you about the build being from an unidentified developer but it will let you run it anyway. Refer to this [article](https://www.howtogeek.com/205393/gatekeeper-101-why-your-mac-only-allows-apple-approved-software-by-default/) for more details.

To run unsigned builds on Windows, double click the .msi installer as usual. In the popup that says "Windows protected your PC", click the "More info" link just below the "Windows protected your PC" text. Then, a button will appear in the bottom right of the popup that says "Run anyway". Click that new "Run anyway" button.

For Linux distributions other than Ubuntu, you will need to [compile Mixxx from source](https://github.com/mixxxdj/mixxx/wiki/compiling-on-Linux) yourself. Refer to the [Using Git](https://github.com/mixxxdj/mixxx/wiki/using-git) wiki page for how to set up Git on your computer for downloading the code to test pull requests.

## Testing Zulip stream

When we need people to test specific pull requests, we will post in the [#testing Zulip stream](https://mixxx.zulipchat.com/#narrow/stream/267968-testing).