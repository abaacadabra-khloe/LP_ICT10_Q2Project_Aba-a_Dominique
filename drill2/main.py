from pyscript import document


def candidate_checker(e):
    club_members = ["jorjor well", "john politics", "doris duinoa", "edgar allan poe", "suwako moriya"]       

    f_name = document.getElementbyId('first name').value
    l_name = document.getElementbyId('last name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on  the list.' , 
                f'Congratulations! {candidate}, you are part of the Literature Club.')

    document.getElementbyId('result').innerHTML = messages[member_checker]
