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

### Sedgewick/Wayne Library

Download the library associated with the Sedgewick and Wayne book, that is, the file [algs4.jar](https://algs4.cs.princeton.edu/code/algs4.jar). Choose a directory where to store the file, for example your home directory `$HOME`. In your `.bashrc`, set your `CLASSPATH` environment variable to `.:$HOME/algs4.jar`. On a UNIX command line with bash, the following would do the job:
```bash
curl -s "https://algs4.cs.princeton.edu/code/algs4.jar" > "$HOME/algs4.jar"
echo 'export CLASSPATH=".:$HOME/algs4.jar"' >> "$HOME/.bashrc"
source "$HOME/.bashrc"
```
On MacOS, the file .`bashrc` is not used. Instead, you need to use `$HOME/.bash_profile` or `$HOME/.profile` in the commands above.

In Windows 10, you can set the CLASSPATH environment variables as follows:
Go to "Control Panel ⇒ System and Security ⇒ System ⇒ Advanced System Settings ⇒ Advanced ⇒ Environment Variables..." and add the correct path (such as `C:\path\to\algs4.jar`) to the "CLASSPATH" variable.

There are other ways of installing algs4.jar, detailed instructions can be found in the middle of [this page](https://algs4.cs.princeton.edu/code/).

### Test that it works

In the end, it is important that you test that Java and the library are correctly installed.
In a command prompt, enter the following:
```bash
java edu.princeton.cs.algs4.Date
```
If everything is installed correctly, this will print a bunch of dates. Otherwise, it will complain with an error message.

## Python

Install Python 3.7 by downloading and running the _Anaconda_ installer appropriate for your operating system from the [anaconda website](https://www.anaconda.com/distribution/).
If you need more instructions, there are some [useful slides](https://learnit.itu.dk/mod/resource/view.php?id=104910).
Note that you must use Python 3 as we rely on some modern Python features, and if you use anything other than Anaconda, that's fine, but do not expect support from TAs or teachers.

After installing Python, enter `python --version` in a command prompt and verify that the version number is correct:
```console
user@host:~$ python --version
Python 3.7.6
```

### Python translation of Sedgewick/Wayne Library

Download and install our translation of Sedgewick and Wayne's library into
Python 3. With Python 3 correctly installed, this should be as easy as running
the following command:

```bash
pip install itu.algs4
```

In case this doesn't quite work, you can find more detailed instructions on
[this page](https://github.com/itu-algorithms/itu.algs4).

### Test that it works

In the end, it is important that you test that Python as well as the library are correctly installed.
In a command prompt, enter the following:
```bash
python -c 'from itu.algs4.stdlib import stdio; stdio.write("Hello World!\n")'
```
If everything is installed correctly, this will print `Hello World!`. Otherwise, it will complain with an error message.

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
