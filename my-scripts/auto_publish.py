def enter_dns_file():
    """
    This function is used to insert de CNAME file into de output folder
    before pushing to GitHub, because afterwards we delete the entire
    output folder.
    """
    with open('output/CNAME', 'w') as f:
        f.write('pablorrobles.com')


def github(publish_drafts=False):
    """
    This function is used tu publish the content of the output folder to
    our GitHub repo, with the option of publishing drafts which is False
    by dafault.
    """
    try:  # Check if we have any drafts in the first place
        if os.path.exists('output/drafts'):
            if not publish_drafts:  # If variable is False we delete them.
                                   # Otherwise we publish the drafts
                local('rm -rf output/drafts')
    except Exception:
        pass

    local('ghp-import output')
    local('git push'
          'git@github.com:pablordrrbl/pablordrrbl.github.io.git'
          'gh-pages:master')
    local('rm -rf output')  # Before doing all the stuff we delete the content
