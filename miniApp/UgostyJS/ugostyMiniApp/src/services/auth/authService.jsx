
export default function getNameFromJwt(jwt) {
    try {
        const decodedToken = JSON.parse(atob(jwt.split(".")[1]));
        const currentUser = decodedToken.username;
        return currentUser;
    }
    catch(e) {
        console.error("Вы не владелец профиля",e);
        return null;

    }

    
}