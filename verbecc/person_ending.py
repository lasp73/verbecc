# -*- coding: utf-8 -*-

class PersonEnding:
    """
    p_elem
    aka <p>
    Ending for a specific verb template, mood, tense and grammatical person
    May also have an alternate ending for an alternative spelling.
    E.g. Ending for aim:er indicatif présent 2nd Person Plural = ['ez']
    E.g. Ending for pa:yer indicatif présent 1st Person Singular = ['ie', 'ye']
    Explanation: 'ye' is an alternate spelling (je paie, je paye)
    p_elem
        Example p_elems:
            <p><i>ez</i></p>
            <p><i>eoir</i><i>oir</i></p>
            <p></p>

    person
    A grammar_defines.PERSONS value indicating which person 
    this PersonEnding is for, e.g. for aim:er, "ez" is '2p' (second person plural)
    """
    def __init__(self, p_elem, person):
        self.person = person
        self.endings = []
        for i_elem in p_elem.findall('i'):
            ending = u''
            if i_elem.text is not None:
                ending += i_elem.text
            self.endings.append(ending)

    def get_person(self):
        return self.person

    def get_ending(self):
        return self.endings[0]

    def get_alternate_ending_if_available(self):
        if len(self.endings) > 1:
            return self.endings[1]
        return self.endings[0]

    def __repr__(self):
        return 'person={} endings={}'.format(self.person, self.endings)
