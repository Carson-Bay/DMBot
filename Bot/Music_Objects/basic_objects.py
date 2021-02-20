import re


class Note:

    def __init__(self, ctx, note_name):

        # Not sure if I need to parse ctx or just get name

        if note_name.isnumeric() and (int(note_name) >= 0 or int(note_name) <= 200):
            # numbered note
            self.note = note_name

        elif note_name.replace('.', '').isnumeric() and (float(note_name.replace('.', '')) >= 0 or float(note_name.replace('.', '')) <= 200):
            # decimal note
            self.note = note_name

        elif len(note_name) == 1 and re.search('[ABCDEFG]', note_name[0]):
            # basic letter note
            self.note = ':' + note_name

        elif len(note_name) == 2 and re.search('[ABCDEFG]', note_name[0]) and (re.search('[bs]', note_name[1]) or re.search('[12345678]', note_name[1])):
            # 2 length letter style
            self.note = ':' + note_name

        elif len(note_name == 3) and re.search('[ABCDEFG]', note_name[0]) and re.search('[bs]', note_name[1]) and re.search('[12345678]', note_name[2]):
            # l3 length letter style
            self.note = ':' + note_name

        else:
            await ctx.channel.send(
                'Error in creating Note:\nTry entering a number between 0 and 200' +
                '\nor a note of the form note|base/sharp|octave#\nExample: Cb3')

    def build(self):
        return self.note


class Chord:  # Will have to fix depending on how I get Data (ctx vs root and chord)
    def __init__(self, ctx, root, chord, pattern='play'):

        # pattern is for arpeggio, timed arpeggio, etc.

        # Error check and make root string
        self.root = Note(root).build()

        # Change as a new feature later
        self.pattern = pattern

        if len(chord) == 1 and re.search('[mM]', chord[0]):
            # major or minor only
            self.chord = ':' + chord

        elif len(chord) > 1 and re.search('[mM]', chord[0]) and chord[1:].isnumeric() and 6 <= int(chord[1:]) <= 13:
            # major or minor with number
            self.chord = ':' + chord

        elif re.search('dim', chord) and chord[3:].isnumeric() and 6 <= int(chord[3:]) <= 13:
            # dim and number
            self.chord = ':' + chord
        elif re.search('dom', chord) and chord[3:].isnumeric() and 6 <= int(chord[3:]) <= 13:
            # dom and number
            self.chord = ':' + chord
        else:
            await ctx.channel.send(
                'Error in creating chord:\nTry entering a note and then an "m" or "M" for minor and major' +
                '\nand optionally, a number between 6 and 13 \nExample: chord Eb3 m13')

    def build(self):

        return self.pattern + 'chord(' + self.root + ', ' + self.chord + ')'


class Track:

    # change error stuff to happen in track so it can await with async
    def __init__(self, items: list, list_order: list = []):
        # --------------------------figure out how to deal with list_order when adding new instances of a note,chord,etc

        self.items = items
        self.list_order = list_order
        pass



    # All these functions will be error checked in music_object_commands
    def add(self, index): # which line

        pass

    def delete(self, index):
        pass

    async def add_sleep(self, index, duration): # index is basically which line of code in a track will be this sleep
        pass



    def build(self):

        str = ''
        for i in self.items:
            str += i.build() + '\n'

        return 'in_thread do\n' + str + '\nend'

