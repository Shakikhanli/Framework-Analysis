


def average_activity(commit_list, activity_bursts, contributor_name):
    commit_count = 0

    for each_activity_bursts in activity_bursts:
        for each_day in each_activity_bursts:
            filtered_list = [commit for commit in commit_list if (commit["date"][:-10] == each_day) and
                             (commit['commit_author']['name'] == contributor_name)]

            commit_count += len(filtered_list)

    average = (commit_count / len(activity_bursts))

    # print('Total count %d ' % commit_count)
    # print('Length of bursts %d ' % len(activity_bursts))
    print('Average activity for contributor "%s" is %f' % (contributor_name, average))



