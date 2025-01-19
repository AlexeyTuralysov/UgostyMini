
import { useEffect, useState } from 'react';

import { useParams } from 'react-router-dom'

import '../../app/styles/pages/Author/Author.scss'
import '../../app/styles/shared/substrate/substrate.scss'
import '../../app/styles/shared/buttons/button.scss'
import AuthorSkeleton from './AuthorSkeleton';

import StatTreats from '../../shared/stats/StatTreats';

import axios from 'axios'
import getNameFromJwt from '../../services/auth/authService';

import { backEnd } from '../settings'
import DonationContainer from './service/DonationContainer';
import DonationContainerBanned from './service/DonationContainerBanned';


import Owner from './owner/Owner';


export default function Author() {
  const { author } = useParams();
 

  const [data, setData] = useState({});


  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);


  const [isOwner, setIsOwner] = useState(false);
  const [isBanned, setIsBanned] = useState(false)





  useEffect(() => {
    const jwt = localStorage.getItem('token');
    const userName = getNameFromJwt(jwt);
  
    //console.log("User Name from JWT:", userName);
    setIsOwner(userName === author);


    axios
      .get(backEnd + `/api/user/${author}`)
      .then((response) => {
        setData(response.data);
        setLoading(false);

        setIsBanned(response.data.status_banned);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
        setError(error);
      });
  }, [author]);




  if (loading) return <div><AuthorSkeleton /></div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <>
      <div>


        

        <div className='user-block'>
          <div className='user-avatar'>
            <img src={data.image} alt={data.nickname} />
          </div>
          <div className='user-name'>
            <span>{data.nickname}</span>
          </div>
          {isOwner && (
          <>

           <Owner author={author}/>

          </>
        )}

          <div className='user-stats'>

            {data.buns && data.buns.map((bunItem, index) => {

              return (
                <StatTreats
                  key={index}
                  count={bunItem.quantity}
                  color={bunItem.bun.color_treats}
                  image={bunItem.bun.img_buns}
                />
              );
            })}
          </div>

          
        </div>

        {isBanned ? (
          <DonationContainerBanned/>
        ) : (
          <DonationContainer userId={data.id} nickname={data.nickname} />
        )}


      </div>




    </>
  );
}