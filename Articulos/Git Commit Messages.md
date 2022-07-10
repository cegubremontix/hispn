## Git Commit Messages

Proposed format of the commit message

```bash
<type>(<optional scope>): <description>

<optional body>

<optional footer>
<fix>: jira-46564
```

All lines are wrapped at 70 characters !

Allowed `<type>`

- feat (feature)
- fix (bug fix)
- docs (documentation)
- style (formatting, missing semi colons, …)
- refactor
- test (when adding missing tests)
- chore (maintain)

**Allowed `<scope>`**

Scope could be anything specifying place of the commit change. For example `$location`, `$browser`, compiler, scope, ng:href, etc...

**Breaking changes**

All breaking changes have to be mentioned in message body, on separated line:

- Breaks removed `$browser.setUrl()` method (use `$browser.url(newUrl)`)

- Breaks ng:repeat option is no longer supported on selects (use `ng:options`)

**Message body**
- uses the imperative, present tense: “change” not “changed” nor “changes”
- includes motivation for the change and contrasts with previous behavior



Modelado a Partir de [Angular Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)

**GIT Commit Quality Message Metrics**

- **Spell metric** : (cantidad de palabras con spelling errors) / (cantidad de palabras totales) **Simple Aproximación**

- **Adherance to format metric** : ❓
  - formato obligatorio
  - tipo obligatorio
  - description: imperative present tense ["change", "add", ... etc]
    
    - [python - NLTK. Detecting whether a sentence is Interogative or Not?](https://stackoverflow.com/questions/49100615/nltk-detecting-whether-a-sentence-is-interogative-or-not/50583762)
    
    - [Natural Language Processing With Python's NLTK Package](https://realpython.com/nltk-nlp-python/)

**Hooks**:

- Verificar cantidad de cambios, reportados y comparados cuando se convierten los archivos al mismo formato.

- Hook para verificar formato del mensaje.
  - Mensaje corto 
  - Mensaje largo
  - git shortlog --author='dvictoriano' (Analiar mis mensajes)

- Crear branch para nuevo jira.
- Crear nuevo archivo con nomemclatura para nuevo script.

[Get commit message in git hook](https://stackoverflow.com/questions/5393178/get-commit-message-in-git-hook)

[Writing Meaningful Commit Messages](https://reflectoring.io/meaningful-commit-messages/)

[How to write meaningful and better commit messages](https://dev.to/rubiin/how-to-write-meaningful-and-better-commit-messages-2d84)

[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

[Semantic Commit Messages](https://sparkbox.com/foundry/semantic_commit_messages)

[Karma - Git Commit Msg](http://karma-runner.github.io/6.3/dev/git-commit-msg.html)

**commit-msg hook**

```bash
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

INPUT_FILE=$1

validate-commit-message.sh $INPUT_FILE

exit $?
```

**validate-commit-message.sh**
```
#!/bin/bash

# Git COMMIT-MSG hook for validating commit message
#See https://docs.google.com/document/d/1rk04jEuGfk9kYzfqCuOlPTSJw3hEDZJTBN5E5f1SALo/edit


MESSAGE=`head -n 1 "$1"`
FOOTER=`tail -n1 "$1"`

echo 
echo 
echo 'salida'
echo $MESSAGE
cat $1
echo $FOOTER
echo
echo

MAX_LENGTH=70
TYPES="chore demo docs feat fix refactor revert style test"
PATTERN="^([a-z]+)\([a-z\0-9\-\*]+\)\:\ (.*)$"
FOOTER_PATTERN="^Fix: [a-z\A-Z]+-[0-9]+$"

if [[ ${#MESSAGE} > $MAX_LENGTH ]]; then
     echo "ERROR: Commit message was ${#MESSAGE} characters long, but should be at most $MAX_LENGTH characters"
     exit 1
fi

if [[ "$MESSAGE" =~ ^WIP ]]; then
    exit 0
fi

if ! [[ "$MESSAGE" =~ $PATTERN ]]; then
    echo "ERROR: Commit message did not match 'type(scope): subject'"
    exit 1
fi

TYPE=${BASH_REMATCH[1]}

if ! [[ $TYPES =~ (^| )$TYPE($| ) ]]; then
    echo "ERROR: Commit message's type '$TYPE' must be one of '$TYPES'"
    exit 1
fi

if ! [[ "$FOOTER" =~ $FOOTER_PATTERN ]]; then
    echo "Error Footer did not match 'Fix: TEXT-NUMBER'"
    exit 1
fi
```
