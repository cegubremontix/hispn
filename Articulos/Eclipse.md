# Eclipse

![Eclipse Architecture](https://www.aosabook.org/images/eclipse/platform.png)

The Eclipse platform is written usign Java  and Java VM is required to run it. It is build from small units of functionality called plugins.

Plugins are the basis of the **Eclipse component model**. A pluging is essentially a JAR file with a manifest which describes itself, its dependencies, and how it can be utilized, or extended.  This manifest information was initiallly stored in a `plug-in.xml` file which resides in teh root of the plugin directory. 

Eclipse plugins are written in Java but could also contain non-code contributions such as HTML files for online documentation.

Each pluging has it's one class loader.

Plugins can express depdendencies on other plugins by the use of `requires` statements in the `plugin.xml`.

**Extention and extention points** : another element of the Eclipse component model. 

One of the most important concepts about Eclipse is that *everything is a plugin*. Whether the plugin is included in the Eclipse platform, or you write it yourself, plugins are all first class components of the assembled application.

The workbench is the most familiar UI element to users of the Eclipse platform, as it provides the structures that organize how Eclipse appears to the user on the desktop. The workbench consists of perspectives, views, and editors. 

- Editors are associated with file types so the correct editor is launched when a file is opened. 
- An example of a view is the "problems" view that indicates errors or warnings in your Java code. 
- Together, editors and views form a perspective which presents the tooling to the user in an organized fashion.


----

The Eclipse workbench is built on the Standard Widget Toolkit (SWT) and JFace, and SWT deserves a bit of exploration. Widget toolkits are generally classified as either native or emulated. 

- **A native widget** toolkit uses operating system calls to build user interface components such as lists and push buttons. Interaction with components is handled by the operating system. An emulated widget toolkit implements components outside of the operating system, handling mouse and keyboard, drawing, focus and other widget functionality itself, rather than deferring to the operating system. Both designs have different strengths and weaknesses.

- **Native widget** toolkits are "pixel perfect." Their widgets look and feel like their counterparts in other applications on the desktop. Operating system vendors constantly change the look and feel of their widgets and add new features. Native widget toolkits get these updates for free. Unfortunately, native toolkits are difficult to implement because their underlying operating system widget implementations are vastly different, leading to inconsistencies and programs that are not portable.

- **Emulated widget** toolkits either provide their own look and feel, or try to draw and behave like the operating system. Their great strength over native toolkits is flexibility (although modern native widget toolkits such as Windows Presentation Framework (WPF) are equally as flexible). Because the code to implement a widget is part of the toolkit rather than embedded in the operating system, a widget can be made to draw and behave in any manner. Programs that use emulated widget toolkits are highly portable. Early emulated widget toolkits had a bad reputation. They were often slow and did a poor job of emulating the operating system, making them look out of place on the desktop. In particular, Smalltalk-80 programs at the time were easy to recognize due to their use of emulated widgets. Users were aware that they were running a "Smalltalk program" and this hurt acceptance of applications written in Smalltalk.

Eclipse uses Apache Lucene to index and search the online help content.

## JDT: Java Development Tools

The JDT provides Java editors, wizards, refactoring support, debugger, compiler and an incremental builder.

Why did the JDT team write a separate compiler to compile your Java code within Eclipse? They had an initial compiler code contribution from VisualAge Micro Edition. They planned to build tooling on top of the compiler, so writing the compiler itself was a logical decision. This approach also allowed the JDT committers to provide extension points for extending the compiler. This would be difficult if the compiler was a command line application provided by a third party.

Locate and take out the **Java Incremental Builder out of eclipse**.

## Plug-in Development Environment (PDE)

The Plug-in Development Environment (PDE) provided the tooling to develop, build, deploy and test plugins and other artifacts that are used to extend the functionality of Eclipse. Since Eclipse plugins were a new type of artifact in the Java world there wasn't a build system that could transform the source into plugins. Thus the PDE team wrote a component called PDE Build which examined the dependencies of the plugins and generated Ant scripts to construct the build artifacts.

With the switch to OSGi, Eclipse plugins became known as bundles. A plugin and a bundle are the same thing: They both provide a modular subset of functionality that describes itself with metadata in a manifest.

## Rich Client Platform (RCP)

- RCP to monitor Mars Rover robots develop by NASA and the Jet Propulsion Laboratory
- Bioclipese for data visualization of bioinformatics
- Dutch Railway for monitorign train performace

## Profiles

A profile is alist of UIs in your install.


## Questions

- How to install pluings
- What are perspectives
- What are workspaces
- How to create new IDE using eclipse as based
- How the eclipse java debugger is implemented
- How eclipse looks for sources
- How eclipse debugger for java looks for sources
- Why project sources and debuggin sources are treaded different in eclipse
- How does Run / Debug configuration in eclipse works?


# Resources

[List of Eclipse-based software](https://en.wikipedia.org/wiki/List_of_Eclipse-based_software)

[The Architecture of Open Source Applications: Eclipse](https://www.aosabook.org/en/eclipse.html)

[Eclipse java debugging: source not found - Stack Overflow](https://stackoverflow.com/questions/6174550/eclipse-java-debugging-source-not-found)

[Eclipse (software)](https://en.wikipedia.org/wiki/Eclipse_(software))

[Standard Widget Toolkit](https://en.wikipedia.org/wiki/Standard_Widget_Toolkit)

[JFace](https://en.wikipedia.org/wiki/JFace)

[Eclipse Equinox](https://en.wikipedia.org/wiki/Equinox_(OSGi))

[Eclipse: A platform for integrating development tools](https://www.ics.uci.edu/~andre/ics228s2006/desriviereswiegand.pdf)

[Using the Eclipse IDE for Java programming - Tutorial](https://www.vogella.com/tutorials/Eclipse/article.html)

[Eclipse Platform Technical Overview](https://www.eclipse.org/articles/Whitepaper-Platform-3.1/eclipse-platform-whitepaper.html)

[Open Services Gateway initiative (OSGI)](https://www.osgi.org/)

[Introduction to OSGi](https://www.baeldung.com/osgi)
