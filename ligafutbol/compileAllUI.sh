#!/usr/bin/env bash
pyrcc5 src/resources.qrc -o gui/resources_rc.py

pyuic5 src/about.ui -o gui/about.py --from-imports
pyuic5 src/capture_webcam_ui.ui -o gui/capture_webcam_ui.py --from-imports
pyuic5 src/clubs_list.ui -o gui/clubs_list.py --from-imports
pyuic5 src/club_edit.ui -o gui/club_edit.py --from-imports
pyuic5 src/main.ui -o gui/main.py --from-imports
pyuic5 src/players_list.ui -o gui/players_list.py --from-imports
pyuic5 src/player_edit.ui -o gui/player_edit.py --from-imports
pyuic5 src/preview_card.ui -o gui/preview_card.py --from-imports




