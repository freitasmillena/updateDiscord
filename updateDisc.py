
import json, argparse

def update_discord_version(new_version):
    
    try:
        with open('/opt/discord/resources/build_info.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print("An error occurred while loading the file:", e)
        return
    data['version'] = new_version
    
    try:
        with open('/opt/discord/resources/build_info.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Discord version successfully updated to", new_version)
    except Exception as e:
        print("An error occurred while updating the version:", e)


parser = argparse.ArgumentParser(description='Update Discord version')
parser.add_argument('-v', type=str, help='The new version to set')
update_discord_version(parser.parse_args().v)
