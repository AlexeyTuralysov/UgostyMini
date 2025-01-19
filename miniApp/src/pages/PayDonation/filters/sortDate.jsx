import moment from 'moment';


export function sortDate({ payloads: dataDonations, filter, count:count }) {

   console.log(count);
    const TimeNow = moment();

    const sortedDonations = [...dataDonations].sort((a, b) => {
        return moment(b.created_at).diff(moment(a.created_at));
    });

    const lastFiveDonations = sortedDonations.slice(0, count);



    const filteredByDate = lastFiveDonations.filter((event) => {
        const eventDate = moment(event.created_at);


        switch (filter) {
            case '1day':
                return eventDate.isAfter(TimeNow.subtract(1, 'days'));


            case '1week':
                return eventDate.isAfter(TimeNow.subtract(1, 'week'));

            case '30days':
                return eventDate.isAfter(TimeNow.subtract(1, 'days'));

            default:
                return true;
        }
    });


    return filteredByDate


}
