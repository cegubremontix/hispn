# Maven

* Non-resolvable parent POM: Hay que configurar el plugin the eclipse mava apuntar a los settings correctamente.
  -  Ademas en eclipse configure a mvn para que se pueda descargar las fuentes automaticamente y asi permitir debuguear.

[Maven: Non-resolvable parnter POM](https://stackoverflow.com/questions/7612309/maven-non-resolvable-parent-pom)

https://github.com/ferstl/depgraph-maven-plugin

[mvnd: Maven's Speed Daemon, a Conversation with Peter Palaga and Guillaume Nodet](https://www.infoq.com/news/2020/12/mvnd-mavens-speed-daemon/)

[Source](https://github.com/apache/maven-mvnd)

- https://github.com/apache/maven
- https://www.mojohaus.org/aspectj-maven-plugin/plugin-info.html
- https://maven.apache.org/plugin-developers/index.html
- https://www.mojohaus.org/aspectj-maven-plugin/compile-mojo.html

##  Glossary

**Project**: Maven things in terms of projects. Everything that you will build are projects. Those projects follow a well defined "Project Object Model". Projects can depend on other projects, in which case the latter are called "dependencies". A project may consist of several subprojects, howerver these subprojects are still treated  equally as projects.

**Project Object Model (POM)**: The Project Object Model, almost always deferred as the POM for brevity, is the metadata that Maven needs to work with your project. Its name is "project.xml" and it is located in the root directory of each projet.

**Artifact**: An artifact is something that is either produced or used by a project. Examples of artifacts produced by Maven for a project include: JARS, source and binary distributions, WARs. Each artifact is identified by a **group id**, an **artifact ID**, a **version**, an **extention  and a classifier** (extention+classifier may be named by a type)

**GroupId**: A group ID a universally unique identifier for a project. Whjile is often just the name, it is helful to use a fully qualified package name to distinguish it from other projects with similar name.

**Dependency**: A typical Java project relies on libraries to build and/or run. Those called "dependencies" inside Maven. Those dependencies are usually other project's JAR artifacts, but are referenced by the POM that describes them.

**Plug-In**: Maven is organized on plugins. Every piece of functionality in Maven is provided by a pluging. Plugins provide goals and use the matadata found in the POM to perform their task. Examples are: jar, eclipse, war. Plugings are primarely written in Java ,mbut Maven also supports writing plug-ins Beanshell and Ant Scripting.

**Mojo**:  A plugin in Java consisnt of one or more mojos. A mojo is a Java class that implements the org.apache.maven.plugin.Mojo interface. This means that a mojo is the implementation for a **goal in a plugin**.

**Repository**: A repostiroy in Maven holds build artifacts and dependencies of varying types: 
- Local,
- Remote

**Snapshots**: Projects can and (should) have a special version includign **SNAPSHOT** to indicate that they are a 'work in progress', and are not yet released. When a snapshopt dependency is encountered, it is always looked for in all remote repositories, and downloaded again if newer than the local copy.

**APT**: APT is a wiki-like format of documentation that Maven currently understands.

**Xdoc**: Xdoc is the format of documentation that Maven currently understand. It is quite simple, and allows embedding XHTML within a simple layout that is transformed into a uniform site.

## Recursos

- [maven - What is the difference between artifactId and groupId in pom.xml? - Stack Overflow](https://stackoverflow.com/questions/39185798/what-is-the-difference-between-artifactid-and-groupid-in-pom-xml)

- [Maven – Glossary](https://maven.apache.org/glossary.html)

- [Maven – Guide to Working with Multiple Modules](https://maven.apache.org/guides/mini/guide-multiple-modules.html)

- [Maven – Maven Getting Started Guide](0https://maven.apache.org/guides/getting-started/index.html)

- [Maven – POM Reference](https://maven.apache.org/pom.html)

- [Maven pom.xml - javatpoint](https://www.javatpoint.com/maven-pom-xml)

- [Maven Tutorial](http://tutorials.jenkov.com/maven/maven-tutorial.html)

- [Maven Tutorial - Tutorialspoint](https://www.tutorialspoint.com/maven/index.htm)

* [Setting the Java Version in Maven | Baeldung](https://www.baeldung.com/maven-java-version)

[Maven is broken by design -  ](http://blog.ltgt.net/maven-is-broken-by-design/)

[Maven: great idea, poor implementation (Part 1) - kief.com -  ](http://kief.com/maven-great-idea-poor-implementation-part-1.html)

[Maven: great idea, poor implementation (Part 2) - kief.com -  ](http://kief.com/maven-great-idea-poor-implementation-part-2.html)

[Maven: great idea, poor implementation (Part 3) - kief.com -  ](http://kief.com/maven-great-idea-poor-implementation-part-3.html)

[We Switched from Maven to Bazel and Builds Got 10x Faster | by Jason Lunz | Code Red -  ](https://redfin.engineering/we-switched-from-maven-to-bazel-and-builds-got-10x-faster-b265a7845854)

[How to get started with Maven | Aditya’s Blog -  ](https://adityasridhar.com/posts/how-to-get-started-with-maven)

[Bazel - a fast, scalable, multi-language and extensible build system" - Bazel -  ](https://bazel.build/)

[java - Maven dependency graph](https://stackoverflow.com/questions/17413089/maven-dependency-graph/34066648)

* [Maven is broken by design](http://blog.ltgt.net/maven-is-broken-by-design/)

* [What is “pom” packaging in maven?](https://stackoverflow.com/questions/7692161/what-is-pom-packaging-in-maven)


In Tech Radar
https://assets.thoughtworks.com/assets/technology-radar-may-2013.pdf

- Maven appert on hold, they recommend gradle.
- Look at the document for a more detailed explanation.


- Maven is a project management tool that provides developers a complete build lifecycle framework.
- Automate the project build infraestructure.
- Maven uses a standard directory layout and a default build lifecycle.

- Maven provides developers ways to manage the following:

1. Builds,
2. Documentation,
3. Reporting,
4. Dependencies,
5. SCMs,
6. Releases,
7. Distribution,
8. Mailing list

Objectives

1. A comrehensive mode for projects, which is reusable, maintainable, and easier to comrehend.
2. Plugins or tools that interact with this declarative model.
Is this really declarative? What is declarative?


Convention over Configuration

${basedir} denotes the project location

Item -> Default
source code -> ${basedir}/src/main/java
Resources -> ${basedir}/src/main/resources
Test -> ${basedir}/src/test
Compiled byte code -> ${basedir}/target
distributable JAR -> ${basedir}/target/classes



Features:

1. Simple project setup.
2. Dependency management including automatic updating.
3. Ability to easiy write plugings in Java or scripting languages.
4. Model-bases builds - Maven is able to build any number of projects into predefined output types such as jar, war, metadata.

5. Coherent side  of project information - Using the same metada as per the build process, maven is able to generate a website and a PDF including complete documentation.

6. Parallel builds - It analyzes the project dependecy graph and enables you to build schedule modules in parallel.

## POM
https://www.tutorialspoint.com/maven/maven_pom.htm


- POM stands for Project Object Model. It is the fundamental unit of work in Maven.
- POM also contains the goals and plugins. While executin a task or goal, Maven looks for te POM in the current directory. It reads te POM, gets the needed configuration information, and then executes the goal Some of the configuration that can be specified in the POM are following

- project depedendencies
- plugins
- goals
- build profiles
- project version
- developers
- mailing list

Before creatinga a POM, we should decide the project **group** (groupId), its name (artifactId) and its version as these attributes hel in uniquely identifyig the project in repostory.

Projects notation in repository is groupId:artifactId:version.

<Tienen una buena explication> ...

Super POM

The super POM is MAVEN's default POM. All POMs inherit from a parent or default (despide explicity defined or not).

Maven uses the effective POM(configuration from super pom plus project configuration) to execute relevant goal.

An easy way to look at the default configurations of the super POM is by running **mvn help:effective-pom**.

## What is a Build Lifecycle?

Maven has the following three standard lifecycles
- clean
- default (or build)
- site

A build lifecycle is a well-defined sequece of phases, which the order in which the goals are to be executed.

A goal represents a specific task which contributes to the building and managing of a project.

- mvn [life cycle]
- mvn [phase or phase:goal], ...

- When a phase is called via Maven command, for example **mvn compile**, only phases up to and including that phase will execute.

- Different maven goals will be bound to different phases of Maven lifecycle deedencing upon the the type or packaging (JAR/WAR/EAR).


## Build Profiles

- Maven build profiles enable you to build your project using different configurations. Instead of creating two separate POM files, you can just specify a profile with the different build configuration, and build your project with this build profile when needed.

- A build profile is a set of configuration values, which be used to set or overrride default values of Maven build.

- Using a build profile, you can customize build for different environments such as Production v/s Development envronments.

Types of Build Profile

- Per project
- Per user
- Global

mvn help:active-profiles

References

- [POM Reference](https://maven.apache.org/pom.html)
- [Maven Tutorial](https://www.tutorialspoint.com/maven/index.htm)
- [Maven Tutorial](http://tutorials.jenkov.com/maven/maven-tutorial.html)



--Notas que he hecho en el trabajo----

- POM (Project Object Model)
    - GroupId (dr)
        - Nota los groupid no puede comensar con do.
    - Artififact Id


- Tree Structure of Projects


- Convention over Modification


- Modulos


- Package:
    - POM
    - JAR
    - EAR
    - ...
 
- Parent


- Phases

- Goles

- Profile


- nvm install -Pdeploy:
    - phase: install
    - Pdeploy: profile


- Orden de prioridad:
    - Hasta ahora creo que el **profile** tiene precedencia antes que **install**.


- Como se empaqueta los **jar|ear|war** y sus depependencias.
    - Las depenencias se ponen en el mismo archivo.


- Install:
    1. compile
    2. package
    3. Instalar en .M2 (carpeta donde se descargan los repositorios en mvn).


- mvn dependencies:source, para descargar las fuentes.


- mvn validate


- SnapShop desarollo (Versiones)


- En jenkins se le quita la etiqueta de snapshop.


- SonaType Nexus -> Mirror Maven Central  y permite compartir internamente.


- Archetype : plantilla pom


- properties - **perfileDespliege** (Why)



- **[Build Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)**:
    - A Build profile is a set of configuration values, which can be used to set or override default values of Maven build. Using a build profile, you can customize build for different environments such as Production v/s Development environments.

- Effective POM.xml vs POM.xml

http://nealford.com/memeagora/2013/01/22/why_everyone_eventually_hates_maven.html
https://martinfowler.com/bliki/InternalReprogrammability.html
Remember that i can do quizzes.


What is a maven repository:

-  a repository is a directory where all the project jars, library jar, plugins or any other project specific artifacts are stored and can be used by Maven easily.

Types:

- local (Maven local repository is a folder location on your machine.)
- central (Maven central repository is repository provided by Maven community. It contains a large number of commonly used libraries.)
- remote (Maven provides concept of Remote Repository, which is developer's own custom repository
containing required libraries or other project jars.)

   <repositories>
      <repository>

Maven Dependency Search Sequence

Step 1 − Search dependency in local repository, if not found, move to step 2 else perform the further processing.

Step 2 − Search dependency in central repository, if not found and remote repository/repositories is/are mentioned then move to step 4. Else it is downloaded to local repository for future reference.

Step 3 − If a remote repository has not been mentioned, Maven simply stops the processing and throws error (Unable to find dependency).

Step 4 − Search dependency in remote repository or repositories, if found then it is downloaded to local repository for future reference. Otherwise, Maven stops processing and throws error (Unable to find dependency).


Maven Plugins

Maven is actually a plugin execution framework where every task is actually done by plugins. Maven Plugins are generally used to −

- create jar file
- create war file
- compile code files
- unit testing of code
- create project documentation
- create project reports

mvn [plugin-name]:[goal-name]
e.j (mvn compiler:compile)

List of plugins:

1. clean
Cleans up target after the build. Deletes the target directory.

2. compiler
Compiles Java source files.

3. surefire
Runs the JUnit unit tests. Creates test reports.

4. jar
Builds a JAR file from the current project.

5. war
Builds a WAR file from the current project.

6. javadoc
Generates Javadoc for the project.

7. antrun
Runs a set of ant tasks from any phase mentioned of the build.

Introduction to the Build Lifecycle

- phases vs goals


## Creating a project (Archetype)

- Maven uses archetype plugins to create projects.
- mvn archetype:generate

## External Dependency

- As you know, Maven does the dependency management using the concept of Repositories. But what happens if dependency is not available in any of remote repositories and central repository? Maven provides answer for such scenario using concept of External Dependency.

- Look at the second dependency element under dependencies in the above example, which clears the following key concepts about External Dependency.

External dependencies (library jar location) can be configured in pom.xml in same way as other dependencies.

Specify groupId same as the name of the library.

Specify artifactId same as the name of the library.

Specify scope as system.

Specify system path relative to the project location.

Hope now you are clear about external dependencies and you will be able to specify external dependencies in your Maven project.

## SNAPSHOT

SNAPSHOT is a special version that indicates a current development copy. Unlike regular versions, Maven checks for a new SNAPSHOT version in a remote repository for every build.

<dependency>
<groupId>data-service</groupId>
<artifactId>data-service</artifactId>
<version>1.0-SNAPSHOT</version>
<scope>test</scope>
</dependency>


## Manage Dependencies

Dependency Scope

1. compile
This scope indicates that dependency is available in classpath of project. It is default scope.

2. provided
This scope indicates that dependency is to be provided by JDK or web-Server/Container at runtime.

3. runtime
This scope indicates that dependency is not required for compilation, but is required during execution.

4. test
This scope indicates that the dependency is only available for the test compilation and execution phases.

5. system
This scope indicates that you have to provide the system path.

6. import
This scope is only used when dependency is of type pom. This scope indicates that the specified POM should be replaced with the dependencies in that POM's <dependencyManagement> section.
