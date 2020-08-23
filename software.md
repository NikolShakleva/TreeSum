# Recommended software

This is an adapted version of the installation guide for the Algorithms and Data Structures Spring course. If your setup worked in that couurse, you are probably good to go. Note that we recommend you install both Java and Python for this course. See the original version here: <https://github.itu.dk/pages/algorithms/ads-2020-notes/preparation/software/>

In general, we discourage using an IDE and instead highly recommend that you work with the command line. We will not need most features that IDEs provide - while IDEs are helpful for large software projects, we consider them a distraction from the content of this course.

This page describes a consistent configuration for each operating system. The goal is to give everyone a UNIX-style command line where you can run Java or Python. The teachers use Linux and MacOS.

## [Windows only] Windows Subsystem for Linux (WSL)

Since you will work with UNIX-based tools (such as bash scripts and the terminal), please install and activate the Linux subsystem in Windows. This is a small Ubuntu distribution that works without the need for a virtual machine or dual-boot. To activate the WSL, follow [these instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and install Ubuntu 18.04.

## Java

We recommend the following route for installing OpenJDK-11, the latest version of Java that has Long-Term Support.
Other versions and variants might or might not work -- if you do not stick to the recommended route, you cannot expect support from TAs or teachers.

- On Windows without WSL: Install it from [adoptopenjdk.net](https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot) with the JVM HotSpot. (If you install Java this way, you can't use the WSL, but must use the Windows command prompt)
- On MacOS, Linux, or in the WSL: Install [sdkman](https://sdkman.io/install), which manages different Java versions and development software. In short, run the following commands in the terminal:

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install java
```

At the time of writing, this should install `11.0.6.hs-adpt`. Important about this is `11` (the latest stable version of Java), `hs` (HotSpot), and `adpt` (AdoptOpenJDK). If sdkman installed any `11.x.y.hs-adpt` version, that's fine. If it installed a significantly different version, look at `sdk list java` for a list of available versions and install the one closest to it using `sdk install java 11.x.y.hs-adpt`.

After installing Java, enter `java -version` in a command prompt and verify that the version number is correct:
```console
user@host:~$ java -version
openjdk version "11.0.6" 2020-01-14
OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.6+10)
OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.6+10, mixed mode)
```

## Python

Install Python 3.7 by downloading and running the _Anaconda_ installer appropriate for your operating system from the [anaconda website](https://www.anaconda.com/distribution/).
If you need more instructions, there are some [useful slides](https://learnit.itu.dk/mod/resource/view.php?id=104910).
Note that you must use Python 3 as we rely on some modern Python features, and if you use anything other than Anaconda, that's fine, but do not expect support from TAs or teachers.

After installing Python, enter `python --version` in a command prompt and verify that the version number is correct:
```console
user@host:~$ python --version
Python 3.7.6
```

## Editor

We are editor-agnostic, that is, we will mainly work with the files directly and consider them to be plain text documents. The role of the editor in this course is just this: edit the content of files.
For this reason, we recommend that you do not use a heavy IDE, but a more light-weight editor.
Nevertheless, syntax highlighting is a nice feature.
The teachers use editors such as `vim` and `emacs`.

Of course, `vim` and `emacs` have a learning curve, so you can use editors such
as Visual Studio Code as well. However, remember that in this course the editor
should just be used to edit files. It is best to compile and run programs from
the command line only.

You can also find an in-depth class that teaches you common command-line tools at <https://missing.csail.mit.edu/>.

## LaTeX

We recommend you to install LaTeX locally on your machine. You can use the `texlive` distribution from <https://tug.org/texlive/>. (Windows users can use texlive from their WSL installation in the same way as Linux users.) Alternatively, you can use https://overleaf.com, which makes collaboration on tex documents very simple.
