void sortCoursesByName(struct Course courses[], int n) {
    struct Course temp;
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (strcmp(courses[j].name, courses[j+1].name) > 0) {
                temp = courses[j];
                courses[j] = courses[j+1];
                courses[j+1] = temp;
            }
        }
    }
}
