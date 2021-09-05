#include <stdlib.h>
#include "sqldump.h"

int main(){
	dead_video_changes();
	player_color();
	the_elite_ltk_videos();
	the_elite_single_segment_videos();
	the_elite_videos();
	tutorial_videos();
}


void dead_video_changes(){
	system("mysqldump -u root -p  dead-video-changes > dead-video-changes/changes.sql");
}

void player_color(){
	system("mysqldump -u root -p  player-colors > player-colors/player_colors.sql");
}

void the_elite_ltk_videos(){
	system("mysqldump -u root -p  the-elite-ltk-videos > the-elite-ltk-videos/dupe_checker.sql");
	system("mysqldump -u root -p  the-elite-ltk-videos > the-elite-ltk-videos/video_data.sql");
}

void the_elite_single_segment_videos(){
	system("mysqldump -u root -p  the-elite-single-segment-videos > the-elite-single-segment-videos/dupe_checker.sql");
	system("mysqldump -u root -p  the-elite-single-segment-videos > the-elite-single-segment-videos/video_data.sql");

}

void the_elite_videos(){
	system("mysqldump -u root -p  the-elite-videos > the-elite-videos/dupe_checker.sql");
	system("mysqldump -u root -p  the-elite-videos > the-elite-videos/video_data.sql");
}

void tutorial_videos(){
	system("mysqldump -u root -p  tutorial-videos > tutorial-videos/goldeneye.sql");
	system("mysqldump -u root -p  tutorial-videos > tutorial-videos/goldeneye_ltk.sql");
	system("mysqldump -u root -p  tutorial-videos > tutorial-videos/miscellaneous_tutorials.sql");
	system("mysqldump -u root -p  tutorial-videos > tutorial-videos/perfect_dark.sql");
	system("mysqldump -u root -p  tutorial-videos > tutorial-videos/perfect_dark_ltk.sql");
}
