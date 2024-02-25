

#
# dutils patch notes

## Version 12.71.2

## Developer(s):
- **formik**
- **deadly**
- **benitas**




## Notes

- **MAJOR + MINOR BUG FIXES**


- **MAJOR CODEBASE REVAMP**

- **SOME DETAILED BUG FIXES**:
        - **_FIXED BUG (ID#1022)_**: Client does not start
\
        - **_FIXED BUG (ID#1020)_**: BLACKCHEAT locks self-bot and forces restart
\
        - **_FIXED BUG (ID#1021)_**: BLACKCHEAT does not do anything
\
        - **_FIXED BUG (ID#1023)_**: JSON Config Parsing Errors


- **OTHER CHANGES**:
        - **_Configuration (`config.json`)_**:
                - `token`: `"token"` -> `"token_file_path"` (requires separate file containing token)
\
                - `message_path`: `"message_path"` -> `"message_file_path"` (requires separate file containing message)
                - `wall_path`: `"wall_path"` -> `"wall_file_path"` (requires separate file containing wall text)
\
                - `post_clear_message_path`: `"post_clear_message_path"` -> `"post_clear_message_file_path"` (requires separate file containing post-clear message; **_can be a blank file_**)
\
                - `blackcheat_words_path`: `"blackcheat_words_path"` -> `"blackcheat_words_list_file_path"` (requires separate file containing list of words; **_should already come pre-packed with dutils_**)
\
        - **_Entry Point / Script (`main.py`)_**: Changed to `"dutils.py"`



<br>
<br>

&ensp;&ensp;&ensp;&ensp;&ensp; ***You are advised to migrate your configuration to this new version.***

#

