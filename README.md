# Action Audit Logger

Experiment with custom python log handling to segment external actions (ie
third party APIs posts) into an auditable log.

Base concept is that actions are logged at `INFO` loglevel, with some
prefix or extra context that allows action log records to be saved in a
dedicated log, without the noise of other records (from any log level, including
INFO).

Ideally the log would specify the action taken and record some state, eg the
endpoint, and either the sent data or the confirmed IDs affected. This might
require saving the logs as something a bit more structured, such as json or even
sqlite.

Inspired partly by a previous encounter with 'xapi' experience logging for
education, which I think I remember takes the form actor/verb/object.

## Background

Reminder: I am approaching this as an experiment, likely to be invalid.

Managing data across two external systems (stock management an online store) is a bit tricky. I would like to be
able to trace any errors resulting from uncaught API failiures etc, without
wedging the custom logging into my business logic.

For the workflow I have in mind performance is not a key factor when compared to
reliability and traceability, so I may be free to consider duplication and
slower writes.

If I do end up with structured log records as an output (json/sqlite) then this
library might also be a good excuse to try out
[textual](https://github.com/Textualize/textual) to create a TUI log
viewer/exporter 😁.
