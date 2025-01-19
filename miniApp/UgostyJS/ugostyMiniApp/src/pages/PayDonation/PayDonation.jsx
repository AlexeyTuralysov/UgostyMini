import { useCallback, useEffect, useState, useMemo } from "react";
import axios from "axios";
import apiClient from "../settings";

import Message from "./messages/Messages";
import "../../app/styles/shared/substrate/substrate_new.scss"

import ChartDate from "../../widgets/Charts/Payers/ChartDate";
import "../../app/styles/shared/select/select.scss"
import "../../app/styles/pages/ProfileManager/Manager.scss"

import moment from 'moment';
import { sortDate } from "./filters/sortDate";

export default function PayDonation() {
    const [dataDonations, setDataDonations] = useState([]);

    const [filter, setfilter] = useState('all');
    const [countFilter, setCountFilter] = useState(5);

    const filteredDonations = useMemo(() => {
        return sortDate({ payloads: dataDonations, filter, count: countFilter });
    }, [dataDonations, filter, countFilter]);

    const getDonationsData = useCallback(async () => {

        await axios
        apiClient.get("/api/user/payments/")
            .then((res) => {
                if (res.data.length > 0) {
                    console.log(res.data);
                    setDataDonations(res.data);
                    console.log("запись данных это рендер");
                }
                else {
                    setDataDonations([]);
                }

            })
            .catch((e) => {

                console.error("ошибка при получении данных:", e);
            });

    }, [])

    useEffect(() => {
        getDonationsData();
    }, [getDonationsData]);

    const handleSelect = useCallback((e) => {
        setfilter(e.target.value);
    }, []);


    return (
        <>
            <div className='content'>
                <h1 className="text">Последние угощения</h1>

                <select className="select" value={filter} onChange={handleSelect}>
                    <option value="all">За все время</option>
                    <option value="1day">За один день</option>
                    <option value="1week">За неделю</option>
                </select>


                <select className="select" value={countFilter} onChange={(e) => setCountFilter(e.target.value)}>
                    <option value={5}>5 последних</option>
                    <option value={10}>10 последних</option>
                    <option value={1000}>Все</option>
                </select>


                <div className="screen-slice " >
                    <div className="block-sp">
                        {filteredDonations && filteredDonations.length > 0 ? (
                            filteredDonations.map((donate) => (
                                <Message
                                    key={donate.id}
                                    socialName={donate.social_media}
                                    message={donate.donation_message}
                                    date={moment(donate.created_at).format('LL')}
                                    pay={donate.payment_amount} />
                            ))
                        ) : (
                            <span>Нет данных</span>
                        )}
                    </div>

                    <div className="sub-statistics">
                        <h3>Статистика</h3>
                        <ChartDate stats={filteredDonations} />
                    </div>

                </div>
            </div>
        </>
    );
}
